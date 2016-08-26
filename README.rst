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

   Ubuntu:

   plugin_dirs = '/usr/local/lib/python2.7/dist-packages/avi/heat'

   RHEL:

   plugin_dirs = '/usr/lib/python2.7/site-packages/avi/heat'

3. Restart heat-engine after adding this:

   e.g., service heat-engine restart


Usage Notes
-----------

For properties that need UUIDs, you can specify a name but prefixed with string "get_avi_uuid_by_name:".
Internally, heat-engine would perform an API call to resolve the provided name into Avi UUID.
For an example usage, please refer to test-member.yaml in examples directory: https://github.com/avinetworks/avi-heat/examples/test-member.yaml.

If you want to provide the name for a UUID property via an input parameter to your template,
please refer to the example in test-member-pool-as-param.yaml: https://github.com/avinetworks/avi-heat/examples/test-member-pool-as-param.yaml.

