from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource


class HealthMonitorHttp(object):
    PROPERTIES = (
        HTTP_REQUEST,
        HTTP_RESPONSE,
        HTTP_RESPONSE_CODE
    ) = ("http_request",
         "http_response",
         "http_response_code")

    properties_schema = {
        HTTP_REQUEST: properties.Schema(
            properties.Schema.STRING,
            _('Request String URL.'),
            required=False,
        ),
        HTTP_RESPONSE: properties.Schema(
            properties.Schema.STRING,
            _('Request String URL.'),
            required=False,
        ),
        HTTP_RESPONSE_CODE: properties.Schema(
            properties.Schema.LIST,
            schema=properties.Schema(
                properties.Schema.STRING,
                _('One of HTTP code types.'),
                constraints=[
                    constraints.AllowedValues([
                        'HTTP_2XX',
                        'HTTP_3XX',
                        'HTTP_4XX',
                        'HTTP_5XX']),
                ]
            ),
            required=False,
        )
    }


class AviHealthMonitor(AviResource):
    """A resource for Avi HealthMonitor
    """

    resource_name = "healthmonitor"

    PROPERTIES = (
        NAME,
        SEND_INTERVAL,
        RECEIVE_TIMEOUT,
        SUCCESSFUL_CHECKS,
        FAILED_CHECKS,
        TYPE,
        HTTP_MONITOR,
    ) = (
        'name',
        'send_interval',
        'receive_timeout',
        'successful_checks',
        'failed_checks',
        'type',
        'http_monitor',
    )

    ATTRIBUTES = (
        NAME_ATTR,
        SEND_INTERVAL_ATTR,
        RECEIVE_TIMEOUT_ATTR,
        SUCCESSFUL_CHECKS_ATTR,
        FAILED_CHECKS_ATTR,
        TYPE_ATTR,
        TENANT_ID,
    ) = (
        'name',
        'send_interval',
        'receive_timeout',
        'successful_checks',
        'failed_checks',
        'type',
        'tenant_id',
    )

    properties_schema = {
        SEND_INTERVAL: properties.Schema(
            properties.Schema.INTEGER,
            _('The minimum time in seconds between regular connections of '
              'the member.'),
            required=True,
            update_allowed=True
        ),
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Name for the health monitor.'),
            required=False,
        ),
        TYPE: properties.Schema(
            properties.Schema.STRING,
            _('One of predefined health monitor types.'),
            required=True,
            constraints=[
                constraints.AllowedValues([
                    'HEALTH_MONITOR_PING',
                    'HEALTH_MONITOR_TCP',
                    'HEALTH_MONITOR_HTTP',
                    'HEALTH_MONITOR_HTTPS']),
            ]
        ),
        FAILED_CHECKS: properties.Schema(
            properties.Schema.INTEGER,
            _('Number of permissible connection failures before changing the '
              'member status to INACTIVE.'),
            required=True,
            update_allowed=True
        ),
        SUCCESSFUL_CHECKS: properties.Schema(
            properties.Schema.INTEGER,
            _('Number of successful checks before changing the '
              'member status to ACTIVE.'),
            required=True,
            update_allowed=True
        ),
        RECEIVE_TIMEOUT: properties.Schema(
            properties.Schema.INTEGER,
            _('Maximum number of seconds for a monitor to wait for a '
              'connection to be established before it times out.'),
            required=True,
            update_allowed=True
        ),
        HTTP_MONITOR: properties.Schema(
            properties.Schema.MAP,
            schema=HealthMonitorHttp.properties_schema,
            description=_('Spec for HTTP monitor if type is HTTP'),
            required=False,
        )
    }

    attributes_schema = {
        NAME_ATTR: attributes.Schema(
            _('The name of the health monitor.'),
            type=attributes.Schema.STRING
        ),
        SEND_INTERVAL_ATTR: attributes.Schema(
            _('The minimum time in seconds between regular connections '
              'of the member.'),
            type=attributes.Schema.STRING
        ),
        SUCCESSFUL_CHECKS_ATTR: attributes.Schema(
            _('Number of permissible connection failures before changing '
              'the member status to INACTIVE.'),
            type=attributes.Schema.STRING
        ),
        RECEIVE_TIMEOUT_ATTR: attributes.Schema(
            _('Maximum number of seconds for a monitor to wait for a '
              'connection to be established before it times out.'),
            type=attributes.Schema.STRING
        ),
        TYPE_ATTR: attributes.Schema(
            _('One of predefined health monitor types.'),
            type=attributes.Schema.STRING
        ),
        TENANT_ID: attributes.Schema(
            _('Tenant owning the health monitor.'),
            type=attributes.Schema.STRING
        ),
    }
