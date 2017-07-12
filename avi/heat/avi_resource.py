import uuid
import logging
import time
from heat.engine import resource
from heat.common import exception as HeatException
from avi_api import ApiSession
from avi_api import ObjectNotFound
import avi_utils

# for python 2/3 compatibility
try:
    basestring
except:
    basestring = str

from oslo_config import cfg
controller_opt = cfg.StrOpt("avi_controller", default="",
                            help="Avi Controller IP or FQDN")
cfg.CONF.register_opt(controller_opt)

LOG = logging.getLogger(__name__)


class AviResource(resource.Resource):
    resource_name = ""  # should be set by derived resource classes

    def get_project_name(self):
        if not self.context.auth_token_info:
            return self.context.tenant
        if "access" in self.context.auth_token_info:
            return self.context.auth_token_info["access"]["token"][
                "tenant"]["name"]
        return self.context.auth_token_info['token']['project']['name']

    def get_user_name(self):
        if not self.context.auth_token_info:
            ksc = self.keystone()
            username = ksc.domain_admin_user
            return username

        if "access" in self.context.auth_token_info:
            user = self.context.auth_token_info["access"]["user"]
        else:
            user = self.context.auth_token_info['token']['user']
        username = user["name"]
        if "domain" in user and user["domain"]["name"] != "Default":
            username += "@%s" % user["domain"]["name"]
        return username

    def get_avi_tenant_uuid(self):
        if self.get_project_name() == 'admin':
            return "admin"
        return avi_utils.os2avi_uuid("tenant",
                                     self.context.tenant_id)

    def get_avi_address(self):
        address = cfg.CONF.avi_controller
        if address:
            return address
        try:
            endpoint = self.client("keystone").url_for(
                service_type="avi-lbaas",
                endpoint_type="publicURL")
            address = endpoint.split("//")[1].split("/")[0]
        except Exception as e:
            LOG.exception("Error during finding avi address: %s", e)
            return None
        return address

    def get_avi_client(self):
        address = self.get_avi_address()
        if not address:
            return None
        username = self.get_user_name()
        password = None
        if not self.context.auth_token:
            password = self.keystone().domain_admin_password
        api_session = ApiSession(
            controller_ip=address,
            username=username,
            token=self.context.auth_token,
            password=password,
        )
        return api_session

    def create_clean_properties(self, inp, field_refs=None, client=None,
                                keyname=None):
        if isinstance(inp, dict):
            newdict = dict()
            newfrefs = field_refs
            if field_refs and keyname and keyname in field_refs:
                newfrefs = field_refs[keyname]
            for k, v in inp.items():
                if v is None:
                    continue
                newdict[k] = self.create_clean_properties(
                    v, field_refs=newfrefs, client=client, keyname=k)
            return newdict
        elif isinstance(inp, list):
            newlist = []
            for entry in inp:
                newlist.append(self.create_clean_properties(
                    entry, field_refs, client, keyname=keyname))
            return newlist
        elif field_refs and isinstance(inp, basestring):
            if keyname and client and inp.startswith("get_avi_uuid_by_name:"):
                objname = inp.split(":", 1)[1]
                resname = field_refs.get(keyname, "").lower()
                if resname:
                    obj = client.get_object_by_name(
                                resname, objname,
                                tenant_uuid=self.get_avi_tenant_uuid()
                            )
                    if not obj:
                        return None
                    return client.get_obj_uuid(obj)
        return inp

    def handle_create(self):
        client = self.get_avi_client()
        res_def = self.create_clean_properties(
            dict(self.properties),
            field_refs=getattr(self, "field_references", {}),
            client=client
        )
        LOG.debug("Resource def for create: %s", res_def)
        try:
            obj = client.post(self.resource_name,
                              data=res_def,
                              tenant_uuid=self.get_avi_tenant_uuid()
                              ).json()
        except Exception as e:
            LOG.exception("Error during creation: %s, resname %s, "
                          "resdef %s headers %s",
                          e, self.resource_name, res_def, client.headers)
            raise
        self.resource_id_set(obj['uuid'])
        return True

    def _show_resource(self, client=None):
        if not client:
            client = self.get_avi_client()
        url = "%s/%s" % (self.resource_name,
                         self.resource_id)
        if self.resource_name in ["virtualservice", "pool"]:
            url += "?join_subresources=runtime"
        obj = client.get(url,
                         tenant_uuid=self.get_avi_tenant_uuid()
                         ).json()
        return avi_utils.replace_refs_with_uuids(obj)

    def _update_obj(self, obj, old_diffs, new_diffs, uniq_keys={}):
        for p in new_diffs.keys():
            prev_val = old_diffs.get(p, None)
            new_val = new_diffs[p]
            if isinstance(new_val, dict) or isinstance(prev_val, dict):
                if not new_diffs[p]:
                    obj.pop(p, None)
                    continue
                if not obj.get(p, None):
                    obj[p] = self.create_clean_properties(new_diffs[p])
                    continue
                if not prev_val:
                    old_diffs[p] = prev_val = dict()
                for k in new_val.keys():
                    if k not in prev_val:
                        prev_val[k] = None
                self._update_obj(obj[p], prev_val, new_val,
                                 uniq_keys=uniq_keys.get(p, {}))
            elif isinstance(new_val, list) or isinstance(prev_val, list):
                # figure out which entries match from old and remove them
                # from obj;
                # then add objects from new_val
                if prev_val and obj.get(p, None):
                    for pitem in prev_val:
                        pitem = self.create_clean_properties(pitem)
                        newobjs = []
                        found = False
                        for oitem in obj[p]:
                            if found:
                                newobjs.append(oitem)
                            elif avi_utils.cmp_a_in_b(pitem, oitem,
                                                      uniq_keys.get(p, {})):
                                found = True
                            else:
                                newobjs.append(oitem)
                        obj[p] = newobjs

                if new_val:
                    obj[p].extend(self.create_clean_properties(new_val))
                else:
                    obj.pop(p, None)
            else:
                if new_diffs[p] is not None:
                    obj[p] = new_diffs[p]
                else:
                    obj.pop(p, None)
        return obj

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        client = self.get_avi_client()
        obj = self._show_resource(client)
        prev_def = self.create_clean_properties(
            dict(self.properties),
            field_refs=getattr(self, "field_references", {}),
            client=client
        )
        # from IPython.core.debugger import Pdb
        # pdb = Pdb()
        # pdb.set_trace()
        self._update_obj(obj, prev_def, prop_diff,
                         uniq_keys=getattr(self, "unique_keys", {}))
        res_def = self.create_clean_properties(
            obj,
            field_refs=getattr(self, "field_references", {}),
            client=client
        )
        try:
            client.put(
                "%s/%s" % (self.resource_name, self.resource_id),
                data=res_def,
                tenant_uuid=self.get_avi_tenant_uuid()
                ).json()
        except:
            LOG.exception("Update failed: (%s, %s): %s",
                          self.resource_name, self.resource_id, res_def)
            raise
        return True

    def handle_delete(self):
        client = self.get_avi_client()
        try:
            client.delete("%s/%s" % (self.resource_name,
                                     self.resource_id),
                          tenant_uuid=self.get_avi_tenant_uuid()
                          ).json()
            if self.resource_name == 'virtualservice':
                LOG.info('await ports cleanup for VS %s', self.resource_id)
                time.sleep(30)
        except ObjectNotFound as e:
            LOG.exception("Object %s not found: %s", (self.resource_name,
                                                      self.resource_id), e)
        return True


class AviNestedResource(AviResource):
    # resoure_name would refer to the top resource that needs to be patched
    # a property with the name resource_name + "_uuid" will be the parent
    #   resource uuid
    # nested_property_name would refer to the name of the property in the
    #   parent resource that needs to be patched
    nested_property_name = ""

    def get_parent_uuid(self):
        parent_uuid_prop = self.resource_name + "_uuid"
        return self.properties[parent_uuid_prop]

    def handle_create(self):
        client = self.get_avi_client()
        res_def = self.create_clean_properties(
            dict(self.properties),
            field_refs=getattr(self, "field_references", {}),
            client=client
        )
        parent_uuid_prop = self.resource_name + "_uuid"
        parent_uuid = res_def[parent_uuid_prop]
        res_def.pop(parent_uuid_prop)
        data = {"update": {self.nested_property_name: [res_def]}}
        try:
            client.patch("%s/%s" % (self.resource_name,
                                    parent_uuid),
                         data=data,
                         tenant_uuid=self.get_avi_tenant_uuid()
                         ).json()
        except Exception as e:
            LOG.exception("Error during creation: %s, resname %s/%s, data %s",
                          e, self.resource_name, parent_uuid, data)
            raise
        return True

    def _show_resource(self, client=None):
        if not client:
            client = self.get_avi_client()
        obj = client.get("%s/%s" % (self.resource_name,
                                    self.get_parent_uuid()),
                         tenant_uuid=self.get_avi_tenant_uuid()
                         ).json()
        return obj

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # force delete and replace
        if not prop_diff:
            return
        if hasattr(HeatException, "UpdateReplace"):
            raise HeatException.UpdateReplace()
        else:  # in older versions
            raise resource.UpdateReplace()

    def handle_delete(self):
        client = self.get_avi_client()
        res_def = self.create_clean_properties(
            dict(self.properties),
            field_refs=getattr(self, "field_references", {}),
            client=client
        )
        parent_uuid_prop = self.resource_name + "_uuid"
        parent_uuid = res_def[parent_uuid_prop]
        if not parent_uuid:
            LOG.info("Parent already deleted!")
            return True
        res_def.pop(parent_uuid_prop)
        data = {"delete": {self.nested_property_name: [res_def]}}
        try:
            client.patch("%s/%s" % (self.resource_name,
                                    parent_uuid),
                         data=data,
                         tenant_uuid=self.get_avi_tenant_uuid()
                         ).json()
        except ObjectNotFound as e:
            LOG.exception("Object %s not found: %s", (self.resource_name,
                                                      parent_uuid), e)
        except Exception as e:
            LOG.exception("Error during deletion: %s, resname %s/%s, data %s",
                          e, self.resource_name, parent_uuid, data)
            raise
        return True
