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
from match import *
from dns import *


class DnsQueryNameMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("Criterion to use for string matching the DNS query domain name in the question section"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['REGEX_MATCH', 'DOES_NOT_END_WITH', 'ENDS_WITH', 'CONTAINS', 'EQUALS', 'DOES_NOT_BEGIN_WITH', 'DOES_NOT_EQUAL', 'REGEX_DOES_NOT_MATCH', 'DOES_NOT_CONTAIN', 'BEGINS_WITH']),
        ],
    )
    query_domain_names_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("Domain name to match against that specified in the question section of the DNS query"),
        required=True,
        update_allowed=False,
    )
    query_domain_names_schema = properties.Schema(
        properties.Schema.LIST,
        _("Domain name to match against that specified in the question section of the DNS query"),
        schema=query_domain_names_item_schema,
        required=False,
        update_allowed=True,
    )
    string_group_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the string group(s) for matching against DNS query domain name in the question section"),
        required=True,
        update_allowed=False,
    )
    string_group_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of the string group(s) for matching against DNS query domain name in the question section You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=string_group_uuids_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'query_domain_names',
        'string_group_uuids',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'query_domain_names': query_domain_names_schema,
        'string_group_uuids': string_group_uuids_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'string_group_uuids': 'stringgroup',
    }



class DnsQueryTypeMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("Criterion to use for matching the DNS query typein the question section"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_NOT_IN', 'IS_IN']),
        ],
    )
    query_type_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS query types in the request query "),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['DNS_RECORD_DNSKEY', 'DNS_RECORD_RRSIG', 'DNS_RECORD_A', 'DNS_RECORD_OTHER', 'DNS_RECORD_AXFR', 'DNS_RECORD_SOA', 'DNS_RECORD_MX', 'DNS_RECORD_SRV', 'DNS_RECORD_HINFO', 'DNS_RECORD_OPT', 'DNS_RECORD_ANY', 'DNS_RECORD_PTR', 'DNS_RECORD_RP', 'DNS_RECORD_TXT', 'DNS_RECORD_AAAA', 'DNS_RECORD_CNAME', 'DNS_RECORD_NS']),
        ],
    )
    query_type_schema = properties.Schema(
        properties.Schema.LIST,
        _("DNS query types in the request query "),
        schema=query_type_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'query_type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'query_type': query_type_schema,
    }




class DnsRuleActionAllowDrop(object):
    # all schemas
    allow_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Allow the DNS query (Default: True)"),
        required=False,
        update_allowed=True,
    )
    reset_conn_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Reset the TCP connection of the DNS query, if allow is set to false to drop the query (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'allow',
        'reset_conn',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'allow': allow_schema,
        'reset_conn': reset_conn_schema,
    }




class DnsRuleActionResponse(object):
    # all schemas
    rcode_schema = properties.Schema(
        properties.Schema.STRING,
        _("DNS response code (Default: DNS_RCODE_NOERROR)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_RCODE_NOERROR', 'DNS_RCODE_RRSET', 'DNS_RCODE_NXDOMAIN', 'DNS_RCODE_YXDOMAIN', 'DNS_RCODE_REFUSED', 'DNS_RCODE_FORMERR', 'DNS_RCODE_NOTIMP', 'DNS_RCODE_NOTZONE', 'DNS_RCODE_SERVFAIL', 'DNS_RCODE_NOTAUTH']),
        ],
    )
    truncation_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("DNS response is truncated (Default: False)"),
        required=False,
        update_allowed=True,
    )
    authoritative_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("DNS response is authoritative (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rcode',
        'truncation',
        'authoritative',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rcode': rcode_schema,
        'truncation': truncation_schema,
        'authoritative': authoritative_schema,
    }




class DnsPolicies(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the dns policy"),
        required=True,
        update_allowed=True,
    )
    dns_policy_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the dns policy You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'dns_policy_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'dns_policy_uuid': dns_policy_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'dns_policy_uuid': 'dnspolicy',
    }



class DnsTransportProtocolMatch(object):
    # all schemas
    match_criteria_schema = properties.Schema(
        properties.Schema.STRING,
        _("Criterion to use for matching the DNS transport protocol"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_NOT_IN', 'IS_IN']),
        ],
    )
    protocol_schema = properties.Schema(
        properties.Schema.STRING,
        _("Protocol to match against transport protocol used by DNS query"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DNS_OVER_UDP', 'DNS_OVER_TCP']),
        ],
    )

    # properties list
    PROPERTIES = (
        'match_criteria',
        'protocol',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'match_criteria': match_criteria_schema,
        'protocol': protocol_schema,
    }




class DnsRuleMatchTarget(object):
    # all schemas
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP addresses to match against client IP"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    protocol_schema = properties.Schema(
        properties.Schema.MAP,
        _("DNS transport protocol match"),
        schema=DnsTransportProtocolMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    query_name_schema = properties.Schema(
        properties.Schema.MAP,
        _("Domain names to match against query name"),
        schema=DnsQueryNameMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    query_type_schema = properties.Schema(
        properties.Schema.MAP,
        _("DNS query types to match against request query type"),
        schema=DnsQueryTypeMatch.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_ip',
        'protocol',
        'query_name',
        'query_type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_ip': client_ip_schema,
        'protocol': protocol_schema,
        'query_name': query_name_schema,
        'query_type': query_type_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'query_name': getattr(DnsQueryNameMatch, 'field_references', {}),
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
        'protocol': getattr(DnsTransportProtocolMatch, 'field_references', {}),
        'query_type': getattr(DnsQueryTypeMatch, 'field_references', {}),
    }



class DnsRuleAction(object):
    # all schemas
    allow_schema = properties.Schema(
        properties.Schema.MAP,
        _("Allow or drop the DNS query"),
        schema=DnsRuleActionAllowDrop.properties_schema,
        required=False,
        update_allowed=True,
    )
    response_schema = properties.Schema(
        properties.Schema.MAP,
        _("Generate a response for the DNS query"),
        schema=DnsRuleActionResponse.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'allow',
        'response',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'allow': allow_schema,
        'response': response_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'response': getattr(DnsRuleActionResponse, 'field_references', {}),
        'allow': getattr(DnsRuleActionAllowDrop, 'field_references', {}),
    }



class DnsRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule (Default: True)"),
        required=False,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=DnsRuleMatchTarget.properties_schema,
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Action to be performed upon successful matching"),
        schema=DnsRuleAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log DNS query upon rule match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'action',
        'log',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'action': action_schema,
        'log': log_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action': getattr(DnsRuleAction, 'field_references', {}),
        'match': getattr(DnsRuleMatchTarget, 'field_references', {}),
    }



class DnsPolicy(AviResource):
    resource_name = "dnspolicy"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the DNS Policy"),
        required=True,
        update_allowed=True,
    )
    rule_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("DNS rules"),
        schema=DnsRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rule_schema = properties.Schema(
        properties.Schema.LIST,
        _("DNS rules"),
        schema=rule_item_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("Creator name"),
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
        'rule',
        'created_by',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'rule': rule_schema,
        'created_by': created_by_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rule': getattr(DnsRule, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::DnsPolicy': DnsPolicy,
    }

