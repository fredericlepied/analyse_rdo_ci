#
# Copyright (C) 2016 Red Hat, Inc.
#
# Author: Frederic Lepied <frederic.lepied@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import classify_log


class TestClassifyLog(unittest.TestCase):

    def test_undercloud(self):
        self.assertEquals(classify_log.classify(POST_INSTALL),
                          ('unknown-column-unique_key-in-field-list',))

    def test_introspection(self):
        self.assertEquals(classify_log.classify(INTROSPECTION),
                          ('introspecting-nodes',))

    def test_overcloudrc(self):
        self.assertEquals(classify_log.classify(MISSING_OVERCLOUDRC),
                          ('overcloudrc-no-such-file-or-directory',))

    def test_resources_error(self):
        self.assertEquals(classify_log.classify(RESOURCES_ERROR),
                          ('no-valid-host-was-found',))

    def test_timeout(self):
        self.assertEquals(classify_log.classify(TIMEOUT),
                          ('create-timed-out',))

POST_INSTALL = '''
+ openstack baremetal import --json instackenv.json
(pymysql.err.InternalError) (1054, u"Unknown column 'unique_key' in 'field list'") [SQL: u'INSERT INTO delayed_calls_v2 (created_at, id, factory_method_path, target_method_name, method_arguments, serializers, unique_key, auth_context, execution_time, processing) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE id=id'] [parameters: (datetime.datetime(2016, 8, 5, 12, 47, 0, 59083), u'06ecd004-26d3-455e-aa7c-93d959c50800', None, 'mistral.engine.actions._run_existing_action', '{"action_ex_id": "57d28243-920d-486b-bf10-1c7ff03bb2b7", "target": null}', None, None, '{"project_name": "admin", "user_id": "bd1a8bf5f6fe4061b1dceed0ec6c843f", "roles": ["admin"], "is_trust_scoped": false, "auth_cacert": null, "auth_token": "d86f785438f0458eb04d637db64f7d13", "auth_uri": "http://192.0.2.1:5000/v3", "service_catalog": "[{\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:5050\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:5050\\", \\"publicURL\\": \\"http://192.0.2.1:5050\\"}], \\"type\\": \\"baremetal-introspection\\", \\"name\\": \\"ironic-inspector\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:6385\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:6385\\", \\"publicURL\\": \\"http://192.0.2.1:6385\\"}], \\"type\\": \\"baremetal\\", \\"name\\": \\"ironic\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"ws://192.0.2.1:9000/\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"ws://192.0.2.1:9000/\\", \\"publicURL\\": \\"ws://192.0.2.1:9000/\\"}], \\"type\\": \\"messaging-websocket\\", \\"name\\": \\"zaqar-websocket\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:8080\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:8080/v1/AUTH_0d1b5970a85c471e9c936eb12dd2c373\\", \\"publicURL\\": \\"http://192.0.2.1:8080/v1/AUTH_0d1b5970a85c471e9c936eb12dd2c373\\"}], \\"type\\": \\"object-store\\", \\"name\\": \\"swift\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:8989/v2\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:8989/v2\\", \\"publicURL\\": \\"http://192.0.2.1:8989/v2\\"}], \\"type\\": \\"workflowv2\\", \\"name\\": \\"mistral\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:9292\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:9292\\", \\"publicURL\\": \\"http://192.0.2.1:9292\\"}], \\"type\\": \\"image\\", \\"name\\": \\"glance\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:8774/v2.1\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:8774/v2.1\\", \\"publicURL\\": \\"http://192.0.2.1:8774/v2.1\\"}], \\"type\\": \\"compute\\", \\"name\\": \\"nova\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:9696\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:9696\\", \\"publicURL\\": \\"http://192.0.2.1:9696\\"}], \\"type\\": \\"network\\", \\"name\\": \\"neutron\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:8888/\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:8888/\\", \\"publicURL\\": \\"http://192.0.2.1:8888/\\"}], \\"type\\": \\"messaging\\", \\"name\\": \\"zaqar\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:35357/v2.0\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:5000/v2.0\\", \\"publicURL\\": \\"http://192.0.2.1:5000/v2.0\\"}], \\"type\\": \\"identity\\", \\"name\\": \\"keystone\\"}, {\\"endpoints\\": [{\\"adminURL\\": \\"http://192.0.2.1:8004/v1/0d1b5970a85c471e9c936eb12dd2c373\\", \\"region\\": \\"regionOne\\", \\"internalURL\\": \\"http://192.0.2.1:8004/v1/0d1b5970a85c471e9c936eb12dd2c373\\", \\"publicURL\\": \\"http://192.0.2.1:8004/v1/0d1b5970a85c471e9c936eb12dd2c373\\"}], \\"type\\": \\"orchestration\\", \\"name\\": \\"heat\\"}]", "project_id": "0d1b5970a85c471e9c936eb12dd2c373", "user_name": "admin"}', datetime.datetime(2016, 8, 5, 12, 47, 0, 56967), 0)]
'''

INTROSPECTION = '''
Exception introspecting nodes: {u'result': u'Failed to run task [wf=WorkflowExecution {\'state_info\': None, \'accepted\': False, \'name\': u\'tripleo.baremetal.v1.introspect\', \'workflow_name\': u\'tripleo.baremetal.v1.introspect\', \'state\': u\'RUNNING\', \'created_at\': \'2016-08-04 11:35:41\', \'tags\': None, \'updated_at\': \'2016-08-04 11:35:41\', \'spec\': {u\'tasks\': {u\'send_message\': {u\'action\': u\'zaqar.queue_post\', u\'input\': {u\'queue_name\': u\'<% $.queue_name %>\', u\'messages\': {u\'body\': {u\'type\': u\'tripleo.baremetal.v1.introspect\', u\'payload\': {u\'status\': u"<% $.get(\'status\', \'SUCCESS\') %>", u\'message\': u"<% $.get(\'message\', \'\') %>", u\'execution\': u\'<% execution() %>\', u\'introspected_nodes\': u"<% $.get(\'introspected_nodes\', []) %>"}}}}, u\'version\': u\'2.0\', u\'type\': u\'direct\', u\'name\': u\'send_message\'}, u\'set_status_failed_start_introspection\': {u\'version\': u\'2.0\', u\'type\': u\'direct\', u\'name\': u\'set_status_failed_start_introspection\', u\'publish\': {u\'status\': u\'FAILED\', u\'message\': u\'<% task(start_introspection).result %>\', u\'introspected_nodes\': []}, u\'on-success\': u\'send_message\'}, u\'wait_for_introspection_to_finish\': {u\'name\': u\'wait_for_introspection_to_finish\', u\'on-success\': u\'send_message\', u\'publish\': {u\'status\': u\'SUCCESS\', u\'message\': u\'Succussfully introspected nodes.\', u\'introspected_nodes\': u\'<% task(wait_for_introspection_to_finish).result %>\'}, u\'version\': u\'2.0\', u\'action\': u\'baremetal_introspection.wait_for_finish\', u\'input\': {u\'uuids\': u\'<% $.node_uuids %>\'}, u\'type\': u\'direct\'}, u\'start_introspection\': {u\'with-items\': u\'uuid in <% $.node_uuids %>\', u\'name\': u\'start_introspection\', u\'on-error\': u\'set_status_failed_start_introspection\', u\'on-success\': u\'wait_for_introspection_to_finish\', u\'version\': u\'2.0\', u\'action\': u\'baremetal_introspection.introspect uuid=<% $.uuid %>\', u\'type\': u\'direct\'}}, u\'description\': u\'Take a list of nodes and move them through introspection.\', u\'version\': u\'2.0\', u\'input\': [u\'node_uuids\', {u\'queue_name\': u\'tripleo\'}], u\'type\': u\'direct\', u\'name\': u\'introspect\'}, \'workflow_id\': u\'87ecf846-1ee3-43a6-a163-6f2735510ccd\', \'params\': {u\'index\': 0, u\'task_execution_id\': u\'ad8f6375-e77d-4f5e-beef-53fdf236e2e1\'}, \'context\': {u\'openstack\': {u\'project_name\': u\'admin\', u\'user_id\': u\'f6d5e896ff1348c99992ba4cb27f21ec\', u\'roles\': [u\'admin\'], u\'is_trust_scoped\': False, u\'auth_cacert\': None, u\'auth_token\': u\'05e3948c20eb43a7b987703841b52695\', u\'auth_uri\': u\'http://192.0.2.1:5000/v3\', u\'service_catalog\': u\'[{"endpoints": [{"adminURL": "http://192.0.2.1:9696", "region": "regionOne", "internalURL": "http://192.0.2.1:9696", "publicURL": "http://192.0.2.1:9696"}], "type": "network", "name": "neutron"}, {"endpoints": [{"adminURL": "http://192.0.2.1:6385", "region": "regionOne", "internalURL": "http://192.0.2.1:6385", "publicURL": "http://192.0.2.1:6385"}], "type": "baremetal", "name": "ironic"}, {"endpoints": [{"adminURL": "http://192.0.2.1:8888/", "region": "regionOne", "internalURL": "http://192.0.2.1:8888/", "publicURL": "http://192.0.2.1:8888/"}], "type": "messaging", "name": "zaqar"}, {"endpoints": [{"adminURL": "http://192.0.2.1:8004/v1/6c2132a27e3345bcb0f40fcca24825a8", "region": "regionOne", "internalURL": "http://192.0.2.1:8004/v1/6c2132a27e3345bcb0f40fcca24825a8", "publicURL": "http://192.0.2.1:8004/v1/6c2132a27e3345bcb0f40fcca24825a8"}], "type": "orchestration", "name": "heat"}, {"endpoints": [{"adminURL": "ws://192.0.2.1:9000/", "region": "regionOne", "internalURL": "ws://192.0.2.1:9000/", "publicURL": "ws://192.0.2.1:9000/"}], "type": "messaging-websocket", "name": "zaqar-websocket"}, {"endpoints": [{"adminURL": "http://192.0.2.1:8989/v2", "region": "regionOne", "internalURL": "http://192.0.2.1:8989/v2", "publicURL": "http://192.0.2.1:8989/v2"}], "type": "workflowv2", "name": "mistral"}, {"endpoints": [{"adminURL": "http://192.0.2.1:9292", "region": "regionOne", "internalURL": "http://192.0.2.1:9292", "publicURL": "http://192.0.2.1:9292"}], "type": "image", "name": "glance"}, {"endpoints": [{"adminURL": "http://192.0.2.1:8774/v2.1", "region": "regionOne", "internalURL": "http://192.0.2.1:8774/v2.1", "publicURL": "http://192.0.2.1:8774/v2.1"}], "type": "compute", "name": "nova"}, {"endpoints": [{"adminURL": "http://192.0.2.1:8080", "region": "regionOne", "internalURL": "http://192.0.2.1:8080/v1/AUTH_6c2132a27e3345bcb0f40fcca24825a8", "publicURL": "http://192.0.2.1:8080/v1/AUTH_6c2132a27e3345bcb0f40fcca24825a8"}], "type": "object-store", "name": "swift"}, {"endpoints": [{"adminURL": "http://192.0.2.1:35357/v2.0", "region": "regionOne", "internalURL": "http://192.0.2.1:5000/v2.0", "publicURL": "http://192.0.2.1:5000/v2.0"}], "type": "identity", "name": "keystone"}, {"endpoints": [{"adminURL": "http://192.0.2.1:5050", "region": "regionOne", "internalURL": "http://192.0.2.1:5050", "publicURL": "http://192.0.2.1:5050"}], "type": "baremetal-introspection", "name": "ironic-inspector"}]\', u\'project_id\': u\'6c2132a27e3345bcb0f40fcca24825a8\', u\'user_name\': u\'admin\'}, u\'__execution\': {u\'input\': {u\'queue_name\': u\'5a04bebf-6e8d-43a2-ae67-3388e0124bcd\', u\'node_uuids\': [u\'f79bb771-a5dc-4c82-8521-bb9750369d5f\', u\'ce16b1bb-2f67-4469-ad55-53cd0cfa35ce\']}, u\'params\': {u\'index\': 0, u\'task_execution_id\': u\'ad8f6375-e77d-4f5e-beef-53fdf236e2e1\'}, u\'id\': u\'02ef40c7-dc61-483e-bb1b-647572d55b92\', u\'spec\': {u\'tasks\': {u\'send_message\': {u\'action\': u\'zaqar.queue_post\', u\'input\': {u\'queue_name\': u\'<% $.queue_name %>\', u\'messages\': {u\'body\': {u\'type\': u\'tripleo.baremetal.v1.introspect\', u\'payload\': {u\'status\': u"<% $.get(\'status\', \'SUCCESS\') %>", u\'message\': u"<% $.get(\'message\', \'\') %>", u\'execution\': u\'<% execution() %>\', u\'introspected_nodes\': u"<% $.get(\'introspected_nodes\', []) %>"}}}}, u\'version\': u\'2.0\', u\'type\': u\'direct\', u\'name\': u\'send_message\'}, u\'set_status_failed_start_introspection\': {u\'version\': u\'2.0\', u\'type\': u\'direct\', u\'name\': u\'set_status_failed_start_introspection\', u\'publish\': {u\'status\': u\'FAILED\', u\'message\': u\'<% task(start_introspection).result %>\', u\'introspected_nodes\': []}, u\'on-success\': u\'send_message\'}, u\'wait_for_introspection_to_finish\': {u\'name\': u\'wait_for_introspection_to_finish\', u\'on-success\': u\'send_message\', u\'publish\': {u\'status\': u\'SUCCESS\', u\'message\': u\'Succussfully introspected nodes.\', u\'introspected_nodes\': u\'<% task(wait_for_introspection_to_finish).result %>\'}, u\'version\': u\'2.0\', u\'action\': u\'baremetal_introspection.wait_for_finish\', u\'input\': {u\'uuids\': u\'<% $.node_uuids %>\'}, u\'type\': u\'direct\'}, u\'start_introspection\': {u\'with-items\': u\'uuid in <% $.node_uuids %>\', u\'name\': u\'start_introspection\', u\'on-error\': u\'set_status_failed_start_introspection\', u\'on-success\': u\'wait_for_introspection_to_finish\', u\'version\': u\'2.0\', u\'action\': u\'baremetal_introspection.introspect uuid=<% $.uuid %>\', u\'type\': u\'direct\'}}, u\'description\': u\'Take a list of nodes and move them through introspection.\', u\'version\': u\'2.0\', u\'input\': [u\'node_uuids\', {u\'queue_name\': u\'tripleo\'}], u\'type\': u\'direct\', u\'name\': u\'introspect\'}}, u\'queue_name\': u\'5a04bebf-6e8d-43a2-ae67-3388e0124bcd\', u\'node_uuids\': [u\'f79bb771-a5dc-4c82-8521-bb9750369d5f\', u\'ce16b1bb-2f67-4469-ad55-53cd0cfa35ce\']}, \'input\': {u\'queue_name\': u\'5a04bebf-6e8d-43a2-ae67-3388e0124bcd\', u\'node_uuids\': [u\'f79bb771-a5dc-4c82-8521-bb9750369d5f\', u\'ce16b1bb-2f67-4469-ad55-53cd0cfa35ce\']}, \'scope\': u\'private\', \'project_id\': u\'6c2132a27e3345bcb0f40fcca24825a8\', \'task_execution_id\': u\'ad8f6375-e77d-4f5e-beef-53fdf236e2e1\', \'id\': u\'02ef40c7-dc61-483e-bb1b-647572d55b92\', \'runtime_context\': {u\'index\': 0}, \'description\': u\'sub-workflow execution\'}, task=wait_for_introspection_to_finish]: Invalid input [name=baremetal_introspection.wait_for_finish, class=NoneType, unexpected=[u\'uuids\']]\nTraceback (most recent call last):\n  File "/usr/lib/python2.7/site-packages/mistral/engine/task_handler.py", line 45, in run_task\n    task.run()\n  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 154, in wrapper\n    return f(*args, **kwargs)\n  File "/usr/lib/python2.7/site-packages/mistral/engine/tasks.py", line 235, in run\n    self._run_new()\n  File "/usr/lib/python2.7/site-packages/mistral/engine/tasks.py", line 266, in _run_new\n    self._schedule_actions()\n  File "/usr/lib/python2.7/site-packages/mistral/engine/tasks.py", line 311, in _schedule_actions\n    action.validate_input(input_dict)\n  File "/usr/lib/python2.7/site-packages/mistral/engine/actions.py", line 285, in validate_input\n    e_utils.validate_input(self.action_def, input_dict)\n  File "/usr/lib/python2.7/site-packages/mistral/engine/utils.py", line 58, in validate_input\n    msg % tuple(msg_props)\nInputException: Invalid input [name=baremetal_introspection.wait_for_finish, class=NoneType, unexpected=[u\'uuids\']]\n'}
Setting nodes for introspection to manageable...
Starting introspection of manageable nodes
Waiting for introspection to finish...
'''

MISSING_OVERCLOUDRC = '''
 overcloud-public-vip
## END OVERCLOUD HOSTS
+ . /home/stack/overcloudrc
/home/stack/overcloud-deploy-post.sh: line 23: /home/stack/overcloudrc: No such file or directory
'''

RESOURCES_ERROR = '''
2016-08-03 10:16:48 [NovaCompute]: CREATE_FAILED ResourceInError: resources.NovaCompute: Went to status ERROR due to "Message: Unknown, Code: Unknown"
2016-08-03 10:16:48 [NovaCompute]: DELETE_IN_PROGRESS state changed
2016-08-03 10:16:49 [Controller]: CREATE_FAILED ResourceInError: resources.Controller: Went to status ERROR due to "Message: No valid host was found. There are not enough hosts available., Code: 500"
'''

TIMEOUT = '''
2016-08-02 11:53:Heat Stack create failed.
36 [ComputeNodesPostDeployment]: CREATE_FAILED CREATE aborted
2016-08-02 11:53:36 [overcloud]: CREATE_FAILED Create timed out
Stack overcloud CREATE_FAILED
'''

if __name__ == "__main__":
    unittest.main()

# test_classify_log.py ends here
