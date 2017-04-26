# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *
from common import *


class UserAccountProfile(AviResource):
    resource_name = "useraccountprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    max_password_history_count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of passwords to be maintained in the password history. Default is 4 passwords. (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    max_login_failure_count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of login attempts before lockout. Default is 3 attempts. (Default: 3)"),
        required=False,
        update_allowed=True,
    )
    account_lock_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Lock timeout period (in minutes). Default is 30 minutes. (Units: MIN) (Default: 30)"),
        required=False,
        update_allowed=True,
    )
    max_concurrent_sessions_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of concurrent sessions allowed. There are unlimited sessions by default. (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    credentials_timeout_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The time period after which credentials expire. Default is 180 days. (Units: DAYS) (Default: 180)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'max_password_history_count',
        'max_login_failure_count',
        'account_lock_timeout',
        'max_concurrent_sessions',
        'credentials_timeout_threshold',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'max_password_history_count': max_password_history_count_schema,
        'max_login_failure_count': max_login_failure_count_schema,
        'account_lock_timeout': account_lock_timeout_schema,
        'max_concurrent_sessions': max_concurrent_sessions_schema,
        'credentials_timeout_threshold': credentials_timeout_threshold_schema,
    }




class Permission(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['WRITE_ACCESS', 'READ_ACCESS', 'NO_ACCESS']),
        ],
    )
    resource_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PERMISSION_SSLPROFILE', 'PERMISSION_ROLE', 'PERMISSION_NETWORK', 'PERMISSION_GSLBSERVICE', 'PERMISSION_GSLB', 'PERMISSION_AUTHPROFILE', 'PERMISSION_VIRTUALSERVICE_MAINTENANCE', 'PERMISSION_EXEMPT', 'PERMISSION_ALERT', 'PERMISSION_CLOUD', 'PERMISSION_MICROSERVICEGROUP', 'PERMISSION_ALERTSYSLOGCONFIG', 'PERMISSION_REBOOT', 'PERMISSION_PRIORITYLABELS', 'PERMISSION_ANALYTICSPROFILE', 'PERMISSION_HTTPPOLICYSET', 'PERMISSION_VRFCONTEXT', 'PERMISSION_APPLICATIONPROFILE', 'PERMISSION_POOLGROUP', 'PERMISSION_VSDATASCRIPTSET', 'PERMISSION_DNSPOLICY', 'PERMISSION_ALERTCONFIG', 'PERMISSION_GSLBGEODBPROFILE', 'PERMISSION_NETWORKPROFILE', 'PERMISSION_SERVICEENGINEGROUP', 'PERMISSION_UPGRADE', 'PERMISSION_IPADDRGROUP', 'PERMISSION_INTERNAL', 'PERMISSION_APPLICATIONPERSISTENCEPROFILE', 'PERMISSION_GSLBHEALTHMONITOR', 'PERMISSION_SNMPTRAPPROFILE', 'PERMISSION_ACTIONGROUPCONFIG', 'PERMISSION_PKIPROFILE', 'PERMISSION_SSLKEYANDCERTIFICATE', 'PERMISSION_CONTROLLER', 'PERMISSION_IPAMDNSPROVIDERPROFILE', 'PERMISSION_HEALTHMONITOR', 'PERMISSION_ALERTEMAILCONFIG', 'PERMISSION_CERTIFICATEMANAGEMENTPROFILE', 'PERMISSION_GSLBAPPLICATIONPERSISTENCEPROFILE', 'PERMISSION_SERVICEENGINE', 'PERMISSION_TENANT', 'PERMISSION_TRAFFIC_CAPTURE', 'PERMISSION_TRAFFICCLONEPROFILE', 'PERMISSION_USER', 'PERMISSION_POOLGROUPDEPLOYMENTPOLICY', 'PERMISSION_VIRTUALSERVICE', 'PERMISSION_POOL', 'PERMISSION_TECHSUPPORT', 'PERMISSION_STRINGGROUP', 'PERMISSION_SYSTEMCONFIGURATION', 'PERMISSION_POOL_MAINTENANCE', 'PERMISSION_NETWORKSECURITYPOLICY']),
        ],
    )

    # properties list
    PROPERTIES = (
        'type',
        'resource',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'resource': resource_schema,
    }




class Role(AviResource):
    resource_name = "role"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    privileges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Permission.properties_schema,
        required=True,
        update_allowed=False,
    )
    privileges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=privileges_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'privileges',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'privileges': privileges_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'privileges': getattr(Permission, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::UserAccountProfile': UserAccountProfile,
        'Avi::LBaaS::Role': Role,
    }

