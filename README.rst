Avi Heat Resources
------------------

Heat resources for Avi Objects

Pre-requisites
--------------

Make sure to have "avi-lbaas" service defined in your keystone catalog.
Please refer to Avi Knowledge Brief at https://kb.avinetworks.com/installing-the-lbaas-driver-cli-shell-openstack/ for details on how to
define this service and an endpoint for it in your keystone catalog.


Installation Steps
------------------

1. Install the AviHeat PIP Package from https://github.com/avinetworks/avi-heat/releases

2. Update your /etc/heat/heat.conf and add the following in [Default] section:

   Ubuntu::

    plugin_dirs = '/usr/local/lib/python2.7/dist-packages/avi/heat'

   RHEL::

    plugin_dirs = '/usr/lib/python2.7/site-packages/avi/heat'

3. Restart heat-engine after adding this. For example::

    $> service heat-engine restart

4. For AutoScalingGroup to work, you need to allow the stack_domain_admin configured
in your /etc/heat.conf to be able to access Avi Controller with Tenant-Admin privileges.

For example, consider the following settings in /etc/heat.conf::

    ...
    stack_domain_admin = heat_domain_admin
    stack_domain_admin_password = abc123
    ...

In this case, you need to create a user named "heat_domain_admin" on Avi Controller
with Tenant-Admin privileges in any tenant, and using the same password as defined
in the heat.conf. The following picture shows how to create such
user in Avi UI.

.. image:: heat_user_on_avi.png
   :scale: 50 %


Alternatively, you can perform a POST API for /api/user URI with the following data
(role_ref needs to be replaced with the url corresponding to the Tenant-Admin role)::
    {
        "username": "heat_domain_admin",
        "password": "abc123",
        "full_name": "Heat Domain Admin",
        "is_active": True,
        "access": [{"all_tenants": True,
                    "role_ref": role_ref}],
        "default_tenant_uuid": "admin",
        "require_password_confirmation": False,
    }


Usage Notes
-----------

Once installed, Heat will expose Avi resource types that users can specify in their heat templates.
For a full list of resource types, use the following command::

    $> heat resource-type-list | grep Avi
    ...
    | Avi::LBaaS::Pool                          |
    | Avi::LBaaS::Pool::Server                  |
    | Avi::LBaaS::Role                          |
    | Avi::LBaaS::SSLProfile                    |
    | Avi::LBaaS::SeProperties                  |
    ...

For a full list of attributes available for any resource type, use the following command::
 
    $> heat resource-type-show Avi::LBaaS::Pool
    ...
     "properties": {
       "lb_algorithm": {
         "description": "The load balancing algorithm will pick a server within the pool's list of available servers.", 
         "required": false, 
         "update_allowed": true, 
         "type": "string", 
         "immutable": false, 
         "constraints": [
           {
             "allowed_values": [
               "LB_ALGORITHM_ROUND_ROBIN", 
               "LB_ALGORITHM_LEAST_LOAD", 
    ...

For properties that need UUIDs, you can specify a name but prefixed with string "get_avi_uuid_by_name:"::

    ...
    member:
      type: Avi::LBaaS::Pool::Server
      properties:
        pool_uuid:  get_avi_uuid_by_name:testpool
    ...

Internally, heat-engine would perform an API call to resolve the provided name into Avi UUID.
For a complete example, please refer to test-member.yaml in examples directory: https://github.com/avinetworks/avi-heat/blob/master/examples/test-member.yaml.


If you want to provide the name for a UUID property via an input parameter to your template,
please refer to the example in test-member-pool-as-param.yaml: https://github.com/avinetworks/avi-heat/blob/master/examples/test-member-pool-as-param.yaml::

    ...
    parameters:
     pool_name:
       type: string
    ...
    resources:
     member:
       type: Avi::LBaaS::Pool::Server
       properties:
         pool_uuid:
           str_replace:
             template: get_avi_uuid_by_name:pname
             params:
               pname: { get_param: pool_name }
    ...

