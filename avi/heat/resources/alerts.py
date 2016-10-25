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


class AlertFilter(object):
    # all schemas
    filter_string_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    filter_action_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'filter_string',
        'filter_action',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'filter_string': filter_string_schema,
        'filter_action': filter_action_schema,
    }




class AlertScriptConfig(AviResource):
    resource_name = "alertscriptconfig"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name of the Script"),
        required=True,
        update_allowed=True,
    )
    action_script_schema = properties.Schema(
        properties.Schema.STRING,
        _("User Defined Alert Action Script. Please refer to kb.avinetworks.com for more information."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'action_script',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'action_script': action_script_schema,
    }




class ActionGroupConfig(AviResource):
    resource_name = "actiongroupconfig"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    email_config_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Select the Email Notification configuration to use when sending alerts via email. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    syslog_config_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Select the Syslog Notification configuration to use when sending alerts via Syslog. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    action_script_config_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("reference of the action script configuration to be used You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    external_only_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Generate Alert only to external destinations"),
        required=True,
        update_allowed=True,
    )
    snmp_trap_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Select the SNMP Trap Notification to use when sending alerts via SNMP Trap. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    autoscale_trigger_notification_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Trigger Notification to AutoScale Manager"),
        required=False,
        update_allowed=True,
    )
    level_schema = properties.Schema(
        properties.Schema.STRING,
        _("When an alert is generated, mark its priority via the Alert Level."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ALERT_LOW', 'ALERT_MEDIUM', 'ALERT_HIGH']),
        ],
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'email_config_uuid',
        'syslog_config_uuid',
        'action_script_config_uuid',
        'external_only',
        'snmp_trap_profile_uuid',
        'autoscale_trigger_notification',
        'level',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'email_config_uuid': email_config_uuid_schema,
        'syslog_config_uuid': syslog_config_uuid_schema,
        'action_script_config_uuid': action_script_config_uuid_schema,
        'external_only': external_only_schema,
        'snmp_trap_profile_uuid': snmp_trap_profile_uuid_schema,
        'autoscale_trigger_notification': autoscale_trigger_notification_schema,
        'level': level_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'email_config_uuid': 'alertemailconfig',
        'action_script_config_uuid': 'alertscriptconfig',
        'syslog_config_uuid': 'alertsyslogconfig',
        'snmp_trap_profile_uuid': 'snmptrapprofile',
    }



class AlertEmailConfig(AviResource):
    resource_name = "alertemailconfig"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name of the email notification service"),
        required=True,
        update_allowed=True,
    )
    to_emails_schema = properties.Schema(
        properties.Schema.STRING,
        _("Alerts are sent to the comma separated list of  email recipients"),
        required=True,
        update_allowed=True,
    )
    cc_emails_schema = properties.Schema(
        properties.Schema.STRING,
        _("Alerts are copied to the comma separated list of  email recipients"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'to_emails',
        'cc_emails',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'to_emails': to_emails_schema,
        'cc_emails': cc_emails_schema,
        'description': description_schema,
    }




class AlertMetricThreshold(object):
    # all schemas
    threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Metric threshold for comparison"),
        required=False,
        update_allowed=True,
    )
    comparator_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ALERT_OP_LE', 'ALERT_OP_GE', 'ALERT_OP_LT', 'ALERT_OP_GT', 'ALERT_OP_NE', 'ALERT_OP_EQ']),
        ],
    )

    # properties list
    PROPERTIES = (
        'threshold',
        'comparator',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'threshold': threshold_schema,
        'comparator': comparator_schema,
    }




class AlertSyslogServer(object):
    # all schemas
    syslog_server_schema = properties.Schema(
        properties.Schema.STRING,
        _("The destination Syslog server IP address or hostname."),
        required=True,
        update_allowed=True,
    )
    syslog_server_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The destination Syslog server's service port."),
        required=False,
        update_allowed=True,
    )
    udp_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Network protocol to establish syslog session"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'syslog_server',
        'syslog_server_port',
        'udp',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'syslog_server': syslog_server_schema,
        'syslog_server_port': syslog_server_port_schema,
        'udp': udp_schema,
    }




class EventDetailsFilter(object):
    # all schemas
    event_details_key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    event_details_value_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    comparator_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ALERT_OP_LE', 'ALERT_OP_GE', 'ALERT_OP_LT', 'ALERT_OP_GT', 'ALERT_OP_NE', 'ALERT_OP_EQ']),
        ],
    )

    # properties list
    PROPERTIES = (
        'event_details_key',
        'event_details_value',
        'comparator',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'event_details_key': event_details_key_schema,
        'event_details_value': event_details_value_schema,
        'comparator': comparator_schema,
    }




class AlertObjectList(AviResource):
    resource_name = "alertobjectlist"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    objects_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['CLIENTSUMMARYINTERNAL', 'SEHEADLESSONLINEREQ', 'INTERFACESUMMARYRUNTIME', 'VIVCENTERDATACENTERS', 'APICTENANTS', 'RTERINGSTATRUNTIME', 'REQUESTQUEUERUNTIME', 'CPUUSAGERUNTIME', 'ALERTPARAMS', 'CONTROLLERPROPERTIES', 'ALERTSYSLOGCONFIG', 'SETROLESREQUEST', 'DISPATCHERSTATRUNTIME', 'SEFAULTINJECTEXHAUSTM', 'RATELIMITERSTATRUNTIME', 'SEAGENTGRAPHDBRUNTIME', 'APPLICATIONPROFILE', 'L7VIRTUALSERVICESTATSRUNTIME', 'SEFAULTINJECTEXHAUSTMCLSMALL', 'METRICSAGENTMESSAGE', 'GSLB', 'STRINGGROUP', 'SEUPGRADESTATUSDETAIL', 'POOLSTATS', 'GSLBDNSUPDATE', 'VSDOSSTATRUNTIME', 'VIHOSTRESOURCES', 'VIRTUALSERVICE', 'VIVCENTERPORTGROUPS', 'SERVERUPDATEREQ', 'SERVERSTATEUPDATEINFO', 'VCENTERMAP', 'POOLGROUP', 'VSCANDIDATESEHOSTLIST', 'APICEPGS', 'DISPATCHERTABLEDUMPRUNTIME', 'DATACENTER', 'MICROSERVICEGROUP', 'LICENSERUNTIME', 'MALLOCSTATRUNTIME', 'VISUBFOLDERS', 'BGPRUNTIME', 'CLUSTER', 'GSLBSERVICE', 'DNSTABLE', 'CLOUD', 'POOLSTATEDBCACHESUMMARY', 'AUTHPROFILE', 'SEAGENTVNICDBRUNTIME', 'SELOGSTATSRUNTIME', 'SEUPGRADESTATUS', 'ACTIONGROUPCONFIG', 'HTTPCACHE', 'APICGRAPHINSTANCES', 'POOLDEBUG', 'CONNECTIONDUMPRUNTIME', 'VIRTUALSERVICEAUTHSTATS', 'METRICSENTITYRUNTIME', 'USER', 'SEMICROSERVICE', 'GSLBSERVICEHMONSTAT', 'VIMGRHOSTRUNTIME', 'IPADDRGROUP', 'SEMEMDISTRUNTIME', 'TRANSACTIONSTATS', 'SEDOSSTATRUNTIME', 'VSSCALEOUTLIST', 'SEAUTHSTATSRUNTIME', 'GSLBHEALTHMONITOR', 'APICTRANSACTION', 'GSLBSITEOPS', 'PKIPROFILE', 'SERUMINSERTIONSTATS', 'METRICSSESTATS', 'HTTPCACHESTATS', 'HTTPPOLICYSETSTATS', 'VIRTUALSERVICEANALYSIS', 'APICAGENTINTERNAL', 'SEGROUPREBALANCE', 'INTERFACERUNTIME', 'SEGROUPUPGRADE', 'MIGRATEALLSTATUSDETAIL', 'NETWORKSECURITYPOLICYDOS', 'SERVERRUNTIME', 'DISPATCHERREMOTETIMERLISTDUMPRUNTIME', 'ENTITYCOUNTERS', 'ARPSTATRUNTIME', 'DEBUGSERVICEENGINE', 'VCENTER', 'NETWORKSECURITYPOLICY', 'VINETWORKSUBNETVMS', 'SEUPGRADE', 'METRICSRUNTIMESUMMARY', 'SECONSUMERPROTO', 'DISPATCHERSEHMPROBETEMPDISABLERUNTIME', 'ARPTABLERUNTIME', 'SECREATEPENDINGPROTO', 'PRIORITYLABELS', 'MICROSERVICEGROUPRUNTIME', 'SHAREDDBSTATSCLEAR', 'PERSISTENCEINTERNAL', 'CLOUDCONNECTOR', 'HEALTHMONITORSTATRUNTIME', 'ALERTTYPECONFIG', 'MICROSERVICERUNTIME', 'SEUPGRADEPREVIEW', 'ALGOSTATRUNTIME', 'CLTRACKSUMMARYINTERNAL', 'IPSTATRUNTIME', 'PLACEMENTSTATS', 'TCPCONNRUNTIMEDETAIL', 'SHMALLOCSTATRUNTIME', 'IPSTKQSTATSRUNTIME', 'APPLICATION', 'TCPCONNRUNTIME', 'SERESERVEDVSCLEAR', 'POOLSERVER', 'VIMGRVCENTERRUNTIME', 'SERESERVEDVS', 'DISPATCHERSTATCLEARRUNTIME', 'NETWORK', 'HEALTHMONITORRUNTIME', 'INTERESTEDVMS', 'HARDWARESECURITYMODULEGROUP', 'VIRTUALMACHINE', 'CONNPOOLINTERNAL', 'PORTGROUP', 'ANALYTICSPROFILE', 'SSLPROFILE', 'ICMPSTATRUNTIME', 'GLBMGRWARMSTART', 'CIFTABLE', 'MIGRATEALL', 'CLOUDCONNECTORUSER', 'ACTIONGROUPPROFILE', 'PLACEMENTSTATUS', 'SSLKEYANDCERTIFICATE', 'UDPSTATRUNTIME', 'POOLGROUPDEPLOYMENTPOLICY', 'HOST', 'CLIENTINTERNAL', 'HEALTHMONITOR', 'HTTPPOLICYSETINTERNAL', 'MICROSERVICE', 'SEVMCREATEPROGRESS', 'TENANT', 'PLACEMENTGLOBALS', 'CPUSTATRUNTIME', 'HTTPPOLICYSET', 'MBSTATRUNTIME', 'CLOUDPROPERTIES', 'SYSTEMCONFIGURATION', 'SERVICEENGINE', 'VSLOGMGRMAP', 'VIRTUALSERVICESTATEDBCACHESUMMARY', 'MIGRATEALLSTATUSSUMMARY', 'APICVMMDOMAINS', 'CLTRACKINTERNAL', 'SEPROPERTIES', 'VSHASHSHOWRUNTIME', 'VRFCONTEXT', 'APICCONFIGURATION', 'SEFAULTINJECTEXHAUSTCONN', 'SERVERSTATEDBCACHESUMMARY', 'APICEPGEPS', 'SHAREDDBSTATS', 'SEFAULTINJECTEXHAUSTMCL', 'KEYVALINTERNAL', 'VIMGRVCENTERCLOUDRUNTIME', 'METRICSRUNTIMEDETAIL', 'MEMINFORUNTIME', 'REBALANCE', 'KEYVALSUMMARYINTERNAL', 'TCPSTATRUNTIME', 'NETWORKSECURITYPOLICYSTATS', 'IPAMPROFILE', 'VIDATASTORE', 'ALERTEMAILCONFIG', 'GSLBSERVICEDETAIL', 'IPAMDNSRECORD', 'CONTROLLERNODE', 'SNMPTRAPPROFILE', 'MAXOBJECTS', 'SERESOURCEPROTO', 'DEBUGCONTROLLER', 'L7GLOBALSTATSRUNTIME', 'VCENTERSUPPORTEDCOUNTERS', 'APICDEVICEPKGVER', 'SEAGENTSTATERUNTIME', 'SEVIPPROTO', 'SERVICEENGINEGROUP', 'VIDATASTORECONTENTS', 'ROUTETABLERUNTIME', 'VSDATASCRIPTSET', 'DEBUGVIRTUALSERVICE', 'SEVSLIST', 'AUTOSCALESTATE', 'APICTRANSACTIONFLAP', 'SERVERAUTOSCALEPOLICY', 'NETWORKSECURITYPOLICYDETAIL', 'SEVM', 'POOL', 'NETWORKPROFILE', 'CONNPOOLSTATS', 'GSLBSERVICERUNTIME', 'GSLBSERVICEINTERNAL', 'ALERTCONFIG', 'ROLE', 'SCHEDULER', 'AUTOSCALELAUNCHCONFIG', 'INTERESTEDHOSTS', 'APPLICATIONPERSISTENCEPROFILE', 'RMVRFPROTO', 'INTERFACELACPRUNTIME']),
        ],
    )
    objects_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=objects_item_schema,
        required=False,
        update_allowed=True,
    )
    source_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['EVENT_LOGS', 'CONN_LOGS', 'APP_LOGS', 'METRICS']),
        ],
    )

    # properties list
    PROPERTIES = (
        'name',
        'objects',
        'source',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'objects': objects_schema,
        'source': source_schema,
    }




class AlertRuleEvent(object):
    # all schemas
    event_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("When the selected event occurs, trigger this alert."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VS_THROUGHPUT_LIMIT', 'GCP_SUBNET_ATTACH_FAIL', 'CONTROLLER_NODE_SHUTDOWN', 'CONTROLLER_LEADER_FAILOVER', 'DEL_NW_SE', 'VINFRA_DISC_NW', 'MESOS_ACCESS_FAILURE', 'APIC_CREATE_LIF_CONTEXTS', 'SYSTEM_UPGRADE_COMPLETE', 'PKT_DROP_NO_PKT_BUFF', 'OPENSTACK_ACCESS_FAILURE', 'SE_GROUP_HOST_DEL', 'CONFIG_CREATE', 'GCP_SUBNET_NOT_FOUND', 'ESX_HOST_UNREACHABLE', 'SE_UPGRADING', 'MIGRATE_SE_STARTED', 'VCA_IMAGE_UPLOAD_SUCCESS', 'SE_EV_GS_GROUP_DOWN', 'APIC_VS_NETWORK_RESOLVE_ERROR', 'POOL_HEALTH_DEGRADED', 'CONTAINER_CLOUD_ACCESS_SUCCESS', 'CC_VNIC_ADDITION_FAILURE', 'CONN_DROP_NO_PKT_BUFF', 'SE_HEALTH_CHANGE', 'CC_VIP_DNS_REGISTER_FAILURE', 'CC_IP_ATTACHED', 'VCA_IMAGE_UPLOAD_FAILURE', 'GSLB_SITE_CFG_STATUS', 'SE_FATAL_ERROR', 'CC_MARATHON_SERVICE_PORT_OUTSIDE_VALID_RANGE', 'SE_SERVER_DELETED', 'VINFRA_DISC_CLUSTER', 'CREATE_SE_FAIL', 'VS_SCALEOUT_FAILED', 'SE_CONN_MEM_HIGH', 'SUMMARIZED_SUBNETS', 'CREATING_SE', 'APIC_DELETE_LIF_CONTEXTS', 'SE_PKT_BUFF_HIGH', 'CC_VNIC_DELETED', 'POOL_HEALTH_CHANGE', 'APIC_DETACH_CIF_FROM_LIF', 'SERVER_AUTOSCALE_IN_COMPLETE', 'OPENSTACK_IP_DETACH_FAILURE', 'CC_SE_STARTED', 'APIC_CREATE_NETWORK', 'PKT_BUFF_ALLOC_FAIL', 'LS_IMAGE_UPLOAD_FAILURE', 'APIC_ATTACH_CIF_TO_LIF', 'GSLB_SITE_EXCEPTION_STATUS', 'CC_SE_CREATION_FAILURE', 'REBALANCE_VS_MIGRATE', 'SE_VNIC_DUPLICATE_IP', 'GCP_ROUTE_DELETE_FAIL', 'LICENSE_EXPIRY', 'OPENSTACK_VNIC_ADDITION_FAILURE', 'CONTROLLER_SERVICE_FAILURE', 'VS_MIGRATE_SCALEOUT_DONE', 'APIC_CREATE_CDEV', 'VS_FSM_DISABLED', 'SE_MEM_HIGH', 'CONN_DROP_NO_CONN_MEM', 'VM_REMOVED', 'REBOOT_SE', 'VS_RPC_TO_RESMGR_FAILED_EVENT', 'SERVER_AUTOSCALE_OUT', 'CONN_DROP_MAX_FLOW_TBL', 'REBALANCE_VS_SCALEOUT', 'SE_REBOOTED', 'CC_SYNC_SERVICES_SUCCESS', 'ROLLBACK_ALL_SE_DONE', 'DOCKER_UCP_IMAGE_UPLOAD_SUCCESS', 'SE_CPU_HIGH', 'SE_GATEWAY_HEARTBEAT_FAILED', 'SSL_CERT_RENEW_FAILED', 'LICENSE_EXPIRED', 'IP_POOL_ALMOST_EXHAUSTED', 'VS_SCALEOUT_COMPLETE', 'CC_CONFIG_FAILURE', 'APIC_BAD_CREDENTIALS', 'APIC_VS_PLACEMENT', 'VCENTER_ADDRESS_ERROR', 'LS_ACCESS_SUCCESS', 'SE_FLOW_TBL_HIGH', 'POOL_SE_HA_COMPROMISED', 'CC_IP_DETACH_FAILURE', 'VCA_ACCESS_FAILURE', 'VS_SCALEIN_ERR', 'CONTAINER_CLOUD_DELETED_SE', 'AVG_UPTIME_CHANGE', 'IP_POOL_EXHAUSTED', 'VS_HEALTH_DEGRADED', 'CREATE_SE_TIMEOUT', 'GCP_ROUTE_DELETE_SUCCESS', 'OPENSTACK_LBPROV_AUDIT_SUCCESS', 'VS_FSM_AWAITING_SE_ASSIGNMENT', 'POOL_UP', 'GSLB_GS_STATUS', 'SE_HEALTH_DEGRADED', 'VS_RPC_TO_SE_FAILED_EVENT', 'MESOS_DELETE_SE_FAIL', 'GCP_ACCESS_FAIL', 'NEW_PROBABLE_SRVR', 'SYSTEM_ROLLBACK_STARTED', 'CONTAINER_CLOUD_IMAGE_UPLOAD_IN_PROGRESS', 'USER_LOGIN', 'VS_RPC_FAILED_EVENT', 'CONTROLLER_WARM_REBOOT', 'CLUSTER_CONFIG_FAILED', 'GS_GROUP_DOWN', 'CONTROLLER_NODE_JOINED', 'UPGRADE_ALL_SE_DONE', 'LS_ACCESS_FAILURE', 'CC_HEALTH_FAILURE', 'VS_SCALEOUT_DONE', 'DOCKER_UCP_ACCESS_FAILURE', 'UPGRADE_SE_VS_MIGRATE', 'RM_DEL_NETWORK_FAIL', 'CC_CLUSTER_VIP_DECONFIG_FAILURE', 'GS_MEMBER_DOWN', 'VS_SE_HA_ACTIVE', 'MESOS_ACCESS_SUCCESS', 'UPGRADE_SE_DONE', 'SE_HM_EVENT_SHM_UP', 'NO_HOST_AVAIL', 'OPENSTACK_VNIC_ADDED', 'CC_CLUSTER_VIP_CONFIG_SUCCESS', 'CC_SE_START_FAILURE', 'MESOS_STOP_SE_FAIL', 'SE_HEALTH_CHECK_FAIL', 'SE_VM_DELETED', 'METRIC_THRESHOLD_UP_VIOLATION', 'SSL_CERT_EXPIRE', 'OPENSTACK_LBPLUGIN_OP_FAILURE', 'SE_VNIC_IP_ADDED', 'CONTAINER_CLOUD_STOP_SE_FAIL', 'CREATED_SE', 'VINFRA_DISC_COMPLETE', 'VS_FSM_INACTIVE', 'SE_EV_GS_MEMBER_UP', 'MIGRATE_SE_RESTARTED', 'REBALANCE_VS_SCALEIN', 'DOCKER_UCP_IMAGE_UPLOAD_FAILURE', 'LICENSE_LIMIT_HOSTS', 'SE_HM_EVENT_SHM_DOWN', 'CLOUDSTACK_ACCESS_FAILURE', 'VS_SCALEIN_FAILED', 'LICENSE_LIMIT_VS', 'MIGRATE_SE_FAILED', 'MESOS_CREATED_SE', 'SE_EV_GS_UP', 'UPGRADE_SE_START', 'SE_ENABLE', 'OPENSTACK_VNIC_REMOVED', 'OPENSTACK_SE_CREATION_FAILURE', 'CONTAINER_CLOUD_IMAGE_UPLOAD_FAILURE', 'CONTAINER_CLOUD_START_SE_FAIL', 'CC_SE_DELETION_FAILURE', 'CONTROLLER_SERVICE_CRITICAL_FAILURE', 'SE_EV_POOL_UP', 'CONFIG_INTERNAL_UPDATE', 'SYSTEM_UPGRADE_ABORTED', 'MESOS_IMAGE_UPLOAD_IN_PROGRESS', 'VS_SE_IP_FAIL', 'OPENSTACK_SE_VM_CREATED', 'GCP_ACCESS_SUCCESS', 'VS_SE_BOOTUP_FAIL', 'OPENSTACK_IMAGE_UPLOAD_SUCCESS', 'APIC_NETWORK_VRF_CHANGED', 'VCENTER_CONNECTIVITY_FAIL', 'SERVER_AUTOSCALE_IN', 'LICENSE_ADDITION_NOTIF', 'MESOS_UPDATED_HOSTS', 'DELETE_SE_FAIL', 'LS_IMAGE_UPLOAD_SUCCESS', 'OPENSTACK_SE_VM_DELETION_DETECTED', 'SCHEDULER_ACTION_SUCCESS', 'LICENSE_LIMIT_THROUGHPUT', 'SE_GROUP_CLUSTER_DEL', 'MIGRATE_SE_VS_MIGRATE_FINISHED', 'CONTAINER_CLOUD_ACCESS_FAILURE', 'SERVER_DELETED', 'APIC_DELETE_NETWORK', 'VS_SCALEIN_DONE_AWAITING_MORE_SE', 'AWS_ACCESS_FAILURE', 'SE_UP', 'SE_MARKED_DOWN', 'SERVER_AUTOSCALE_FAILED', 'MODIFY_NW', 'VS_MIGRATE_SCALEOUT_ERROR', 'SE_HEARTBEAT_FAILURE', 'CC_SE_STOP_FAILURE', 'OPENSTACK_VNIC_DELETION_FAILURE', 'CC_SE_STOPPED', 'GS_DOWN', 'SE_EV_VS_UP', 'CONN_DROP_MAX_SYN_TBL', 'CC_DELETE_VIP_FAILURE', 'CONTROLLER_NODE_DB_REPLICATION_FAILED', 'POOL_DOWN', 'SCHEDULER_ACTION_FAILURE', 'OPENSTACK_IP_DETACHED', 'CC_IP_ATTACH_FAILURE', 'LICENSE_LIMIT_SERVERS', 'VS_INITIAL_PLACEMENT_FAILED', 'SE_VNIC_IP_REMOVED', 'OPENSTACK_SYNC_SERVICES_FAILURE', 'SE_VNIC_DOWN_EVENT', 'SE_HM_EVENT_GHM_UP', 'CC_CLUSTER_VIP_CONFIG_FAILURE', 'CONTAINER_CLOUD_IMAGE_UPLOAD_SUCCESS', 'CACHE_OBJ_ALLOC_FAIL', 'CC_UPDATE_VIP_FAILURE', 'VS_SCALEIN_COMPLETE', 'CONFIG_DELETE', 'APIC_DELETE_LIFS', 'CONFIG_UPDATE', 'AWS_IMAGE_UPLOAD_SUCCESS', 'SE_VERSION_CHECK_FAILED', 'CONTAINER_CLOUD_CREATE_SE_FAIL', 'MESOS_IMAGE_UPLOAD_FAILURE', 'DELETED_SE', 'CLOUDSTACK_IMAGE_UPLOAD_FAILURE', 'CONFIG_ACTION', 'APIC_DELETE_CDEV', 'SERVER_AUTOSCALE_OUT_COMPLETE', 'VCENTER_CONNECTIVITY_SUCCESS', 'GCP_ROUTE_ADD_FAIL', 'SE_PERSIST_TBL_HIGH', 'GSLB_SITE_OPER_STATUS', 'ADD_NW_FAIL', 'OPENSTACK_SE_VM_DELETED', 'MESOS_START_SE_FAIL', 'MESOS_STOPPED_SE', 'SERVER_HEALTH_CHANGE', 'DOCKER_UCP_IMAGE_UPLOAD_IN_PROGRESS', 'CC_SE_DELETED', 'SE_SYN_TBL_HIGH', 'SERVER_UP_HA_ACTIVE', 'SE_DP_HB_FAILED', 'CLOUDSTACK_IMAGE_UPLOAD_SUCCESS', 'GCP_API_FAIL', 'APIC_DELETE_TENANT', 'VS_MIGRATE_SCALEIN_ERROR', 'SERVER_HEALTH_DEGRADED', 'MODIFY_NW_FAIL', 'SE_GATEWAY_HEARTBEAT_SUCCESS', 'SE_DOS_ATTACK', 'CONTAINER_CLOUD_STARTED_SE', 'VS_FSM_ACTIVE', 'CONTAINER_CLOUD_SERVICE_FAILURE', 'VS_ADD_SE', 'CONTROLLER_NODE_STARTED', 'OPENSTACK_ACCESS_SUCCESS', 'OPENSTACK_IMAGE_UPLOAD_FAILURE', 'MESOS_IMAGE_UPLOAD_SUCCESS', 'MGMT_NW_DEL', 'SE_SERVER_APP_CHANGED', 'UPGRADE_ALL_SE_NOT_NEEDED', 'SE_SERVER_DISABLED', 'VS_FSM_PERMANENT_ERROR', 'APIC_CREATE_LIFS', 'CC_VNIC_ADDED', 'SERVER_AUTOSCALE_OUT_FAILED', 'MIGRATE_SE_VS_MIGRATE_FAILED', 'OPENSTACK_LBPLUGIN_OP_SUCCESS', 'SERVER_DOWN', 'CC_SE_DELETION_DETECTED', 'CONTAINER_CLOUD_SERVICE_SUCCESS', 'CC_VNIC_DELETION_FAILURE', 'DISCOVERY_DATACENTER_DEL', 'APIC_CREATE_TENANT', 'DUPLICATE_SUBNETS', 'GCP_SE_DETECTED', 'SSL_CERT_RENEW', 'USER_LOGOUT', 'MGMT_NW_NAME_CHANGED', 'SE_EV_GS_DOWN', 'METRICS_DB_DISK_FULL', 'ESX_HOST_POWERED_DOWN', 'SYSTEM_UPGRADE_STARTED', 'SE_DOWN', 'CC_SE_CREATED', 'VS_FSM_UNEXPECTED_EVENT', 'ADD_VIP_VNIC', 'LICENSE_LIMIT_SE_SOCKETS', 'VINFRA_DISC_DC', 'CONTAINER_CLOUD_DELETE_SE_FAIL', 'GS_MEMBER_UP', 'VS_MIGRATE_FAILED', 'VS_UP', 'SYSTEM_ROLLBACK_COMPLETE', 'VS_REMOVED_SE_INT', 'SE_EV_GS_GROUP_DELETED', 'VS_MIGRATE_COMPLETE', 'MESOS_STARTED_SE', 'GS_GROUP_UP', 'VS_MIGRATE_STARTED', 'VS_FSM_TRANSIENT_ERROR', 'CC_GENERIC_FAILURE', 'CC_MARATHON_SERVICE_PORT_ALREADY_IN_USE', 'VCENTER_ACCESS_SLOW', 'CC_CLUSTER_VIP_DECONFIG_SUCCESS', 'SE_EV_SERVER_DOWN', 'VS_AWAITING_SE', 'DOS_ATTACK', 'SE_POOL_DELETED', 'VS_REMOVED_SE', 'POOL_SE_HA_ACTIVE', 'VS_SCALEOUT_DONE_AWAITING_MORE_SE', 'MIGRATE_SE_VS_MIGRATE_STARTED', 'SE_MIGRATE', 'OPENSTACK_TENANTS_DELETED', 'GS_UP', 'SE_EXTERNAL_HM_RESTART', 'ROLLBACK_ALL_SE_START', 'POOL_AUTO_DEPLOYMENT_FAILED', 'OPENSTACK_LBPROV_AUDIT_FAILURE', 'VS_FSM_PARTITIONED', 'SE_EV_GS_GROUP_UP', 'GSLB_DNS_STATUS', 'USER_PASSWORD_CHANGE_REQUEST', 'VS_SE_HA_COMPROMISED', 'VINFRA_DISC_VM', 'OPENSTACK_SYNC_SERVICES_SUCCESS', 'LICENSE_LIMIT_SE_VCPUS', 'POOL_AUTO_DEPLOYMENT_SUCCESS', 'SE_HM_EVENT_GHM_DOWN', 'OPENSTACK_IP_ATTACH_FAILURE', 'CLOUDSTACK_ACCESS_SUCCESS', 'AWS_ACCESS_SUCCESS', 'DOCKER_UCP_ACCESS_SUCCESS', 'CC_SYNC_SERVICES_FAILURE', 'VS_FSM_ACTIVE_AWAITING_SCALEOUT_READY', 'VS_DOWN', 'MESOS_DELETED_SE', 'VS_ADD_SE_INT', 'CONTAINER_CLOUD_UPDATED_HOSTS', 'SE_POWERED_DOWN', 'MESOS_CREATE_SE_FAIL', 'VS_SCALEOUT_ERR', 'SERVER_UP', 'CC_TENANT_INIT_FAILURE', 'SERVER_AUTOSCALE_IN_FAILED', 'DEL_VIP_VNIC', 'VINFRA_DISC_FAILURE', 'VCA_ACCESS_SUCCESS', 'VS_MIGRATE_SCALEIN_DONE', 'SSL_KEY_EXPORTED', 'CONTROLLER_NODE_LEFT', 'CONN_DROP_POOL_LB_FAILURE', 'CONTAINER_CLOUD_CREATED_SE', 'VINFRA_DISC_HOST', 'CC_IP_DETACHED', 'UPGRADE_SE_VS_DISRUPTED', 'SE_EV_GS_MEMBER_DOWN', 'UPGRADE_SE_NOT_NEEDED', 'SE_GROUP_MGMT_NW_DEL', 'SE_VNIC_DHCP_IP_ALLOC_FAILURE', 'SERVER_DOWN_HA_COMPROMISED', 'UPGRADE_ALL_SE_START', 'UPGRADE_SE_VS_SCALEIN', 'APIC_BIND_VNIC_TO_NETWORK', 'ADD_NW_SE', 'SE_EV_SERVER_UP', 'VS_FSM_ACTIVE_AWAITING_SE_TRANSITION', 'VS_MIGRATE_DONE', 'CONFIG_INTERNAL_CREATE', 'UPGRADE_SE_VS_SCALEOUT', 'CONTROLLER_SERVICE_RESTORED', 'AWS_IMAGE_UPLOAD_FAILURE', 'OPENSTACK_SE_DELETION_FAILURE', 'DELETING_SE', 'VS_CONN_LIMIT', 'CONN_DROP_MAX_PERSIST_TBL', 'SYSTEM_ROLLBACK_ABORTED', 'VS_HEALTH_CHANGE', 'SE_DISK_HIGH', 'GCP_ROUTE_ADD_SUCCESS', 'ANOMALY', 'VS_SWITCHOVER', 'CONTAINER_CLOUD_STOPPED_SE', 'SE_EV_POOL_DOWN', 'OPENSTACK_IP_ATTACHED', 'VCENTER_BAD_CREDENTIALS', 'VM_ADDED', 'VCENTER_VERSION_NOT_SUPPORTED', 'CC_HEALTH_OK', 'SE_EV_VS_DOWN', 'VS_SCALEIN_DONE', 'CC_DECONFIG_FAILURE', 'SE_SYN_CACHE_USAGE_HIGH', 'LICENSE_REMOVAL_NOTIF', 'MIGRATE_SE_FINISHED', 'VS_SWITCHOVER_FAIL', 'SE_VM_PURGED']),
        ],
    )
    not_cond_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    event_details_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=EventDetailsFilter.properties_schema,
        required=True,
        update_allowed=False,
    )
    event_details_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=event_details_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'event_id',
        'not_cond',
        'event_details',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'event_id': event_id_schema,
        'not_cond': not_cond_schema,
        'event_details': event_details_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'event_details': getattr(EventDetailsFilter, 'field_references', {}),
    }



class AlertSyslogConfig(AviResource):
    resource_name = "alertsyslogconfig"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name of the syslog notification"),
        required=True,
        update_allowed=True,
    )
    syslog_servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertSyslogServer.properties_schema,
        required=True,
        update_allowed=False,
    )
    syslog_servers_schema = properties.Schema(
        properties.Schema.LIST,
        _("The list of syslog servers"),
        schema=syslog_servers_item_schema,
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("User defined description for alert syslog config"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'syslog_servers',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'syslog_servers': syslog_servers_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'syslog_servers': getattr(AlertSyslogServer, 'field_references', {}),
    }



class AlertRuleMetric(object):
    # all schemas
    metric_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("Metric Id for the Alert. Eg. l4_client.avg_complete_conns"),
        required=False,
        update_allowed=True,
    )
    metric_threshold_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertMetricThreshold.properties_schema,
        required=True,
        update_allowed=True,
    )
    duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Evaluation window for the Metrics"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'metric_id',
        'metric_threshold',
        'duration',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'metric_id': metric_id_schema,
        'metric_threshold': metric_threshold_schema,
        'duration': duration_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'metric_threshold': getattr(AlertMetricThreshold, 'field_references', {}),
    }



class AlertRule(object):
    # all schemas
    sys_event_rule_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertRuleEvent.properties_schema,
        required=True,
        update_allowed=False,
    )
    sys_event_rule_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=sys_event_rule_item_schema,
        required=False,
        update_allowed=True,
    )
    conn_app_log_rule_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertFilter.properties_schema,
        required=False,
        update_allowed=True,
    )
    event_match_filter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    metrics_rule_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AlertRuleMetric.properties_schema,
        required=True,
        update_allowed=False,
    )
    metrics_rule_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=metrics_rule_item_schema,
        required=False,
        update_allowed=True,
    )
    operator_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['OPERATOR_AND', 'OPERATOR_OR']),
        ],
    )

    # properties list
    PROPERTIES = (
        'sys_event_rule',
        'conn_app_log_rule',
        'event_match_filter',
        'metrics_rule',
        'operator',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'sys_event_rule': sys_event_rule_schema,
        'conn_app_log_rule': conn_app_log_rule_schema,
        'event_match_filter': event_match_filter_schema,
        'metrics_rule': metrics_rule_schema,
        'operator': operator_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'sys_event_rule': getattr(AlertRuleEvent, 'field_references', {}),
        'metrics_rule': getattr(AlertRuleMetric, 'field_references', {}),
        'conn_app_log_rule': getattr(AlertFilter, 'field_references', {}),
    }



class AlertConfig(AviResource):
    resource_name = "alertconfig"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the alert configuration"),
        required=True,
        update_allowed=True,
    )
    summary_schema = properties.Schema(
        properties.Schema.STRING,
        _("Summary of reason why alert is generated"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _("A custom description field."),
        required=False,
        update_allowed=True,
    )
    alert_rule_schema = properties.Schema(
        properties.Schema.MAP,
        _("list of filters matching on events or client logs used for triggering alerts."),
        schema=AlertRule.properties_schema,
        required=True,
        update_allowed=True,
    )
    threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("An alert is created only when the number of events meets or exceeds this number within the chosen time frame."),
        required=False,
        update_allowed=True,
    )
    throttle_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config."),
        required=False,
        update_allowed=True,
    )
    rolling_window_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Only if the Number of Events is reached or exceeded within the Time Window will an alert be generated."),
        required=False,
        update_allowed=True,
    )
    expiry_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("An alert is expired and deleted after the expiry time has elapsed.  The original event triggering the alert remains in the event's log."),
        required=False,
        update_allowed=True,
    )
    source_schema = properties.Schema(
        properties.Schema.STRING,
        _("Signifies system events or the type of client logsused in this alert configuration"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['EVENT_LOGS', 'CONN_LOGS', 'APP_LOGS', 'METRICS']),
        ],
    )
    obj_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the resource for which alert was raised"),
        required=False,
        update_allowed=True,
    )
    category_schema = properties.Schema(
        properties.Schema.STRING,
        _("Determines whether an alert is raised as soon as the event occurs (Realtime) or the Controller should wait until the specified number of events has occured in the rolling window's time interval."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['ROLLINGWINDOW', 'REALTIME', 'WATERMARK']),
        ],
    )
    recommendation_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable this alert config from generating new alerts."),
        required=False,
        update_allowed=True,
    )
    action_group_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("The alert config will trigger the selected alert action, which send send notifications or execute custom scripts. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    autoscale_alert_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("This alert config applies to auto scale alerts"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'summary',
        'description',
        'alert_rule',
        'threshold',
        'throttle',
        'rolling_window',
        'expiry_time',
        'source',
        'obj_uuid',
        'category',
        'recommendation',
        'enabled',
        'action_group_uuid',
        'autoscale_alert',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'summary': summary_schema,
        'description': description_schema,
        'alert_rule': alert_rule_schema,
        'threshold': threshold_schema,
        'throttle': throttle_schema,
        'rolling_window': rolling_window_schema,
        'expiry_time': expiry_time_schema,
        'source': source_schema,
        'obj_uuid': obj_uuid_schema,
        'category': category_schema,
        'recommendation': recommendation_schema,
        'enabled': enabled_schema,
        'action_group_uuid': action_group_uuid_schema,
        'autoscale_alert': autoscale_alert_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action_group_uuid': 'actiongroupconfig',
        'alert_rule': getattr(AlertRule, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::AlertSyslogConfig': AlertSyslogConfig,
        'Avi::LBaaS::AlertScriptConfig': AlertScriptConfig,
        'Avi::LBaaS::AlertObjectList': AlertObjectList,
        'Avi::LBaaS::AlertConfig': AlertConfig,
        'Avi::LBaaS::ActionGroupConfig': ActionGroupConfig,
        'Avi::LBaaS::AlertEmailConfig': AlertEmailConfig,
    }

