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
from match import *


class FullClientLogs(object):
    # all schemas
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Capture all client logs including connections and requests.  When disabled, only errors will be logged. (Default: False)"),
        required=True,
        update_allowed=True,
    )
    duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("How long should the system capture all logs, measured in minutes. Set to 0 for infinite. (Units: MIN) (Default: 30)"),
        required=False,
        update_allowed=True,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log all headers. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'enabled',
        'duration',
        'all_headers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'enabled': enabled_schema,
        'duration': duration_schema,
        'all_headers': all_headers_schema,
    }




class MetricsRealTimeUpdate(object):
    # all schemas
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enables real time metrics collection.  When disabled, 6 hour view is the most granular the system will track. (Default: False)"),
        required=True,
        update_allowed=True,
    )
    duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Real time metrics collection duration in minutes. 0 for infinite. (Units: MIN) (Default: 30)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'enabled',
        'duration',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'enabled': enabled_schema,
        'duration': duration_schema,
    }




class ClientLogFilter(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(" (Default: False)"),
        required=False,
        update_allowed=True,
    )
    uri_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=StringMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(" (Default: False)"),
        required=True,
        update_allowed=True,
    )
    duration_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 30)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'name',
        'client_ip',
        'all_headers',
        'uri',
        'enabled',
        'duration',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'name': name_schema,
        'client_ip': client_ip_schema,
        'all_headers': all_headers_schema,
        'uri': uri_schema,
        'enabled': enabled_schema,
        'duration': duration_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
        'uri': getattr(StringMatch, 'field_references', {}),
    }



class ClientInsightsSampling(object):
    # all schemas
    skip_uris_schema = properties.Schema(
        properties.Schema.MAP,
        _("URL patterns to avoid when inserting RUM script."),
        schema=StringMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    sample_uris_schema = properties.Schema(
        properties.Schema.MAP,
        _("URL patterns to check when inserting RUM script."),
        schema=StringMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("Client IP addresses to check when inserting RUM script."),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'skip_uris',
        'sample_uris',
        'client_ip',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'skip_uris': skip_uris_schema,
        'sample_uris': sample_uris_schema,
        'client_ip': client_ip_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'skip_uris': getattr(StringMatch, 'field_references', {}),
        'client_ip': getattr(IpAddrMatch, 'field_references', {}),
        'sample_uris': getattr(StringMatch, 'field_references', {}),
    }



class AnalyticsPolicy(object):
    # all schemas
    full_client_logs_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=FullClientLogs.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_log_filters_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ClientLogFilter.properties_schema,
        required=True,
        update_allowed=False,
    )
    client_log_filters_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=client_log_filters_item_schema,
        required=False,
        update_allowed=True,
    )
    client_insights_schema = properties.Schema(
        properties.Schema.STRING,
        _("Gain insights from sampled client to server HTTP requests and responses. (Default: ACTIVE)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PASSIVE', 'ACTIVE', 'NO_INSIGHTS']),
        ],
    )
    metrics_realtime_update_schema = properties.Schema(
        properties.Schema.MAP,
        _("Settings to turn on realtime metrics and set duration for realtime updates"),
        schema=MetricsRealTimeUpdate.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_insights_sampling_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ClientInsightsSampling.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'full_client_logs',
        'client_log_filters',
        'client_insights',
        'metrics_realtime_update',
        'client_insights_sampling',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'full_client_logs': full_client_logs_schema,
        'client_log_filters': client_log_filters_schema,
        'client_insights': client_insights_schema,
        'metrics_realtime_update': metrics_realtime_update_schema,
        'client_insights_sampling': client_insights_sampling_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'client_log_filters': getattr(ClientLogFilter, 'field_references', {}),
        'metrics_realtime_update': getattr(MetricsRealTimeUpdate, 'field_references', {}),
        'client_insights_sampling': getattr(ClientInsightsSampling, 'field_references', {}),
        'full_client_logs': getattr(FullClientLogs, 'field_references', {}),
    }

