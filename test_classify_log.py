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

    def test_heat(self):
        self.assertEquals(classify_log.classify(HEAT_RESOURCE),
                          ('os-cinder-volume',))

    def test_heat2(self):
        self.assertEquals(classify_log.classify(HEAT_RESOURCE2),
                          ('os-cinder-volume',))

    def test_tempest(self):
        self.assertEquals(classify_log.classify(TEMPEST),
                          ('/home/stack/tempest_console.log',))

    def test_tempest_failed(self):
        self.assertEquals(
            classify_log.classify(TEMPEST_FAILED),
            ('tempest',
             'api.volume.test_volumes_list.VolumesV2ListTestJSON'))

    def test_create_failed(self):
        self.assertEquals(
            classify_log.classify(CREATE_FAILED),
            ('/home/stack/failed_deployment_list.log',))

    def test_failed_deployment(self):
        self.assertEquals(
            classify_log.classify(FAILED_DEPLOYMENT_lIST),
            ('swift-service-end',))

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

HEAT_RESOURCE = '''
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+-----------------+---------------------+--------------+
| resource_name         | physical_resource_id                                                                | resource_type                | resource_status | updated_time        | stack_name   |
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+-----------------+---------------------+--------------+
| key_pair              | pingtest_key                                                                        | OS::Nova::KeyPair            | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| private_net           | 620b3db4-68f6-49b5-84c2-8d264509d4a0                                                | OS::Neutron::Net             | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| private_subnet        | e78d6050-dccd-42f4-b8fd-bf27f668cdb6                                                | OS::Neutron::Subnet          | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| router                | bb87d5d3-749b-4f6d-9609-082d7b358bdb                                                | OS::Neutron::Router          | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| router_interface      | bb87d5d3-749b-4f6d-9609-082d7b358bdb:subnet_id=e78d6050-dccd-42f4-b8fd-bf27f668cdb6 | OS::Neutron::RouterInterface | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| server1               |                                                                                     | OS::Nova::Server             | INIT_COMPLETE   | 2016-08-09T02:46:58 | tenant-stack |
| server1_floating_ip   | 8de47108-cf61-465d-b885-a5827a402c20                                                | OS::Neutron::FloatingIP      | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| server1_port          | 33b6a864-b8e4-4fe1-a0b8-12ffc56e9296                                                | OS::Neutron::Port            | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| server_security_group | 0434542a-1e9f-4b8c-9f74-b8282e2a7ec2                                                | OS::Neutron::SecurityGroup   | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| test_flavor           | f9e78e3e-f678-41cc-be51-3fda1434e3c2                                                | OS::Nova::Flavor             | CREATE_COMPLETE | 2016-08-09T02:46:58 | tenant-stack |
| volume1               | d1733b4d-519e-4288-b584-65f4a9194f33                                                | OS::Cinder::Volume           | CREATE_FAILED   | 2016-08-09T02:46:58 | tenant-stack |
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+-----------------+---------------------+--------------+
'''

HEAT_RESOURCE2 = '''
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+--------------------+---------------------+--------------+
| resource_name         | physical_resource_id                                                                | resource_type                | resource_status    | updated_time        | stack_name   |
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+--------------------+---------------------+--------------+
| key_pair              | pingtest_key                                                                        | OS::Nova::KeyPair            | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| router                | fd786e39-fbbd-4f11-8104-68a4d22a2614                                                | OS::Neutron::Router          | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| router_interface      | fd786e39-fbbd-4f11-8104-68a4d22a2614:subnet_id=51fb28c4-9ca4-43cf-87aa-2b61bb67d585 | OS::Neutron::RouterInterface | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| server1               |                                                                                     | OS::Nova::Server             | INIT_COMPLETE      | 2016-08-08T23:51:27 | tenant-stack |
| server1_floating_ip   | 39b7d1cd-4b72-48c2-8b7b-13eb317f685a                                                | OS::Neutron::FloatingIP      | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| server1_port          | 201ef053-2f84-4b12-b7a6-d083f47162fd                                                | OS::Neutron::Port            | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| test_flavor           | 07c831f1-64b0-4573-bf3c-6e0fb37c8784                                                | OS::Nova::Flavor             | CREATE_COMPLETE    | 2016-08-08T23:51:27 | tenant-stack |
| volume1               | b084f9a1-a414-4b3a-b5f7-a06a57b42fb2                                                | OS::Cinder::Volume           | CREATE_IN_PROGRESS | 2016-08-08T23:51:27 | tenant-stack |
| private_net           | e9554296-9950-4d5e-8dba-73946a87a4b7                                                | OS::Neutron::Net             | CREATE_COMPLETE    | 2016-08-08T23:51:28 | tenant-stack |
| private_subnet        | 51fb28c4-9ca4-43cf-87aa-2b61bb67d585                                                | OS::Neutron::Subnet          | CREATE_COMPLETE    | 2016-08-08T23:51:28 | tenant-stack |
| server_security_group | 042b0d2a-a6c6-47fb-8526-f316b193753d                                                | OS::Neutron::SecurityGroup   | CREATE_COMPLETE    | 2016-08-08T23:51:28 | tenant-stack |
+-----------------------+-------------------------------------------------------------------------------------+------------------------------+--------------------+---------------------+--------------+
'''

TEMPEST = '''
++ find /home/stack/tempest/.testrepository -name '[0-9]'
+ subunit2html /home/stack/tempest/.testrepository/0 /home/stack/tempest.html
+ exit 1
'''

TEMPEST_FAILED = '''
{0} setUpClass (tempest.api.volume.test_volumes_list.VolumesV1ListTestJSON) [0.000000s] ... FAILED
{0} setUpClass (tempest.scenario.test_server_multinode.TestServerMultinode) ... SKIPPED: Less than 2 compute nodes, skipping multinode tests.
{1} setUpClass (tempest.api.volume.test_volumes_list.VolumesV2ListTestJSON) [0.000000s] ... FAILED
{1} tempest.scenario.test_server_basic_ops.TestServerBasicOps.test_server_basic_ops [41.543969s] ... ok
'''

CREATE_FAILED = '''
ver failed: deploy_status_code: Deployment exited with non-zero status code: 6
2016-08-09 15:35:21 [overcloud-ControllerNodesPostDeployment-2ktulx3uomb2]: CREATE_FAILED Resource CREATE failed: Error: resources.ControllerOvercloudServicesDeployment_Step4.resources[0]: Deployment to server failed: deploy_status_code: Deployment exited with non-zero status code: 6
2016-08-09 15:35:22 [ControllerNodesPostDeployment]: CREATE_FAILED Error: resources.ControllerNodesPostDeployment.resources.ControllerOvercloudServicesDeployment_Step4.resources[0]: Deployment to server failed: deploy_status_code: Deployment exited with non-zero status code: 6
2016-08-09 15:35:22 [overcloud]: CREATE_FAILED Resource CREATE failed: Error: resources.ControllerNodesPostDeployment.resources.ControllerOvercloudServicesDeployment_Step4.resources[0]: Deployment to server failed: deploy_status_code: Deployment exited with non-zero status code: 6
Stack overcloud CREATE_FAILED
'''

FAILED_DEPLOYMENT_lIST = '''
 deploy_stderr: |
    ...
    [1;31mWarning: /Stage[main]/Swift::Storage::Account/Swift::Storage::Generic[account]/Swift::Service[swift-account-server]/Service[swift-account-server]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Object/Swift::Storage::Generic[object]/Swift::Service[swift-object-replicator]/Service[swift-object-replicator]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Object/Swift::Storage::Generic[object]/Swift::Service[swift-object-auditor]/Service[swift-object-auditor]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Proxy/Swift::Service[swift-proxy-server]/Service[swift-proxy-server]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Object/Swift::Service[swift-object-updater]/Service[swift-object-updater]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Container/Swift::Storage::Generic[container]/Swift::Service[swift-container-replicator]/Service[swift-container-replicator]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Container/Swift::Storage::Generic[container]/Swift::Service[swift-container-auditor]/Service[swift-container-auditor]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Container/Swift::Storage::Generic[container]/Swift::Service[swift-container-server]/Service[swift-container-server]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Storage::Container/Swift::Service[swift-container-updater]/Service[swift-container-updater]: Skipping because of failed dependencies[0m
    [1;31mWarning: /Stage[main]/Swift::Deps/Anchor[swift::service::end]: Skipping because of failed dependencies[0m
    (truncated, view all with --long)
'''

if __name__ == "__main__":
    unittest.main()

# test_classify_log.py ends here
