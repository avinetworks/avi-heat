# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *


class SeResources(object):
    # all schemas
    num_vcpus_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    memory_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    disk_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    hyper_threading_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    sockets_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cores_per_socket_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'num_vcpus',
        'memory',
        'disk',
        'hyper_threading',
        'sockets',
        'cores_per_socket',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'num_vcpus': num_vcpus_schema,
        'memory': memory_schema,
        'disk': disk_schema,
        'hyper_threading': hyper_threading_schema,
        'sockets': sockets_schema,
        'cores_per_socket': cores_per_socket_schema,
    }



class ConServer(object):
    # all schemas
    server_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    virtual_network_id_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    virtual_network_id_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=virtual_network_id_item_schema,
        required=False,
        update_allowed=True,
    )
    subnet_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    subnet_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=subnet_item_schema,
        required=False,
        update_allowed=True,
    )
    pool_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server_ip',
        'virtual_network_id',
        'subnet',
        'pool_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server_ip': server_ip_schema,
        'virtual_network_id': virtual_network_id_schema,
        'subnet': subnet_schema,
        'pool_uuid': pool_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'subnet': getattr(IpAddrPrefix, 'field_references', {}),
        'server_ip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'subnet': getattr(IpAddrPrefix, 'unique_keys', {}),
        'server_ip': getattr(IpAddr, 'unique_keys', {}),
    }



class MemberInterface(object):
    # all schemas
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    active_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'if_name',
        'active',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'if_name': if_name_schema,
        'active': active_schema,
    }

    unique_keys = {
        'my_key': 'if_name',
    }



class ServiceEngine(AviResource):
    resource_name = "serviceengine"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    se_group_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    enable_state_schema = properties.Schema(
        properties.Schema.STRING,
        _("inorder to disable SE set this field appropriately"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SE_STATE_DISABLED', 'SE_STATE_DISABLED_FOR_PLACEMENT', 'SE_STATE_ENABLED']),
        ],
    )

    # properties list
    PROPERTIES = (
        'name',
        'se_group_uuid',
        'enable_state',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'se_group_uuid': se_group_uuid_schema,
        'enable_state': enable_state_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'se_group_uuid': 'serviceenginegroup',
    }



class ConVip(object):
    # all schemas
    vip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    virtual_network_id_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    virtual_network_id_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=virtual_network_id_item_schema,
        required=False,
        update_allowed=True,
    )
    subnet_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    subnet_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=subnet_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vip',
        'virtual_network_id',
        'subnet',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vip': vip_schema,
        'virtual_network_id': virtual_network_id_schema,
        'subnet': subnet_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'subnet': getattr(IpAddrPrefix, 'field_references', {}),
        'vip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'subnet': getattr(IpAddrPrefix, 'unique_keys', {}),
        'vip': getattr(IpAddr, 'unique_keys', {}),
    }



class vNICNetwork(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    ctlr_alloc_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    mode_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DHCP', 'VIP', 'STATIC', 'DOCKER_HOST']),
        ],
    )

    # properties list
    PROPERTIES = (
        'ip',
        'ctlr_alloc',
        'mode',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'ctlr_alloc': ctlr_alloc_schema,
        'mode': mode_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddrPrefix, 'field_references', {}),
    }

    unique_keys = {
        'ip': getattr(IpAddrPrefix, 'unique_keys', {}),
        'my_key': 'ip',
    }



class ConInfo(object):
    # all schemas
    con_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    vip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ConVip.properties_schema,
        required=True,
        update_allowed=True,
    )
    servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ConServer.properties_schema,
        required=True,
        update_allowed=False,
    )
    servers_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=servers_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'con_uuid',
        'vip',
        'servers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'con_uuid': con_uuid_schema,
        'vip': vip_schema,
        'servers': servers_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'vip': getattr(ConVip, 'field_references', {}),
        'servers': getattr(ConServer, 'field_references', {}),
    }

    unique_keys = {
        'vip': getattr(ConVip, 'unique_keys', {}),
        'servers': getattr(ConServer, 'unique_keys', {}),
    }



class VlanInterface(object):
    # all schemas
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    vlan_id_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    dhcp_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    vnic_networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=vNICNetwork.properties_schema,
        required=True,
        update_allowed=False,
    )
    vnic_networks_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=vnic_networks_item_schema,
        required=False,
        update_allowed=True,
    )
    vrf_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'if_name',
        'vlan_id',
        'dhcp_enabled',
        'vnic_networks',
        'vrf_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'if_name': if_name_schema,
        'vlan_id': vlan_id_schema,
        'dhcp_enabled': dhcp_enabled_schema,
        'vnic_networks': vnic_networks_schema,
        'vrf_uuid': vrf_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'vrf_uuid': 'vrfcontext',
        'vnic_networks': getattr(vNICNetwork, 'field_references', {}),
    }

    unique_keys = {
        'my_key': 'if_name',
        'vnic_networks': getattr(vNICNetwork, 'unique_keys', {}),
    }



class vNIC(object):
    # all schemas
    dhcp_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    vnic_networks_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=vNICNetwork.properties_schema,
        required=True,
        update_allowed=False,
    )
    vnic_networks_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=vnic_networks_item_schema,
        required=False,
        update_allowed=True,
    )
    vrf_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    vlan_interfaces_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VlanInterface.properties_schema,
        required=True,
        update_allowed=False,
    )
    vlan_interfaces_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=vlan_interfaces_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'dhcp_enabled',
        'enabled',
        'vnic_networks',
        'vrf_uuid',
        'vlan_interfaces',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'dhcp_enabled': dhcp_enabled_schema,
        'enabled': enabled_schema,
        'vnic_networks': vnic_networks_schema,
        'vrf_uuid': vrf_uuid_schema,
        'vlan_interfaces': vlan_interfaces_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'vlan_interfaces': getattr(VlanInterface, 'field_references', {}),
        'vrf_uuid': 'vrfcontext',
        'vnic_networks': getattr(vNICNetwork, 'field_references', {}),
    }

    unique_keys = {
        'vlan_interfaces': getattr(VlanInterface, 'unique_keys', {}),
        'my_key': 'if_name',
        'vnic_networks': getattr(vNICNetwork, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::ServiceEngine': ServiceEngine,
    }

