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

import classify_console as classify


class TestClassify(unittest.TestCase):

    def test_undercloud(self):
        self.assertEquals(classify.classify(RECAP_UNDERCLOUD), ('undercloud',))

    def test_postinstall(self):
        self.assertEquals(classify.classify(RECAP_POSTINSTALL),
                          ('undercloud_post_install',
                           '/home/stack/undercloud_post_install.log'))

    def test_host(self):
        self.assertEquals(classify.classify(RECAP_HOST), ('host',))

    def test_host_error(self):
        self.assertEquals(classify.classify(RECAP_HOST_ERROR),
                          ('host',
                           'failed-to-connect-to-the-hypervisor'))

    def test_unreachable(self):
        self.assertEquals(classify.classify(RECAP_UNREACHABLE),
                          ('undercloud',
                           'failed-to-connect-to-the-host-via-ssh'))

    def test_missing_file(self):
        self.assertEquals(
            classify.classify(MISSING_FILE),
            ('host',
             'minimal_pacemaker.yml-does-not-exist-or-is-not-readable',))

    def test_hung_up(self):
        self.assertEquals(
            classify.classify(HUNG_UP),
            ('host',
             'the-remote-end-hung-up-unexpectedly',))

    def test_remote_host(self):
        self.assertEquals(
            classify.classify(REMOTE_HOST),
            ('host',
             'remote-host-identification-has-changed',))

    def test_slave_offline(self):
        self.assertEquals(
            classify.classify(SLAVE_OFFLINE),
            ('host',
             'slave-went-offline-during-the-build',))

    def test_tempest(self):
        self.assertEquals(
            classify.classify_stderr(TEMPEST.split('\n')),
            ('host', 'tempest', 'VPNaaSTestJSON'))

    def test_summary(self):
        self.assertEquals(
            classify.classify_stderr(PACKSTACK_SUMMARY.split('\n')),
            ('host', 'running-tempest'))

RECAP_UNDERCLOUD = '''
PLAY RECAP *********************************************************************
172.19.2.138               : ok=79   changed=50   unreachable=0    failed=0   
localhost                  : ok=15   changed=7    unreachable=0    failed=0   
undercloud                 : ok=12   changed=9    unreachable=0    failed=1   

'''

RECAP_POSTINSTALL = '''
TASK [tripleo/undercloud : Prepare the undercloud for deploy] ******************
task path: /home/rhos-ci/workspace/tripleo-quickstart-promote-master-delorean-minimal/tripleo-quickstart/roles/tripleo/undercloud/tasks/post-install.yml:27
Thursday 04 August 2016  11:33:57 +0000 (0:00:00.308)       0:31:48.576 ******* 
fatal: [undercloud]: FAILED! => {"changed": true, "cmd": "/home/stack/undercloud-post-install.sh > /home/stack/undercloud_post_install.log 2>&1", "delta": "0:01:52.246180", "end": "2016-08-04 11:35:50.722169", "failed": true, "rc": 1, "start": "2016-08-04 11:33:58.475989", "stderr": "", "stdout": "", "stdout_lines": [], "warnings": []}

PLAY RECAP *********************************************************************
172.19.2.138               : ok=79   changed=50   unreachable=0    failed=0   
localhost                  : ok=15   changed=7    unreachable=0    failed=0   
undercloud                 : ok=12   changed=9    unreachable=0    failed=1   

'''

RECAP_HOST = '''
PLAY RECAP *********************************************************************
172.19.2.133               : ok=70   changed=43   unreachable=0    failed=1   
localhost                  : ok=9    changed=4    unreachable=0    failed=0   

'''

RECAP_HOST_ERROR = '''
TASK [setup/undercloud : Create undercloud volume] *****************************
task path: /home/rhos-ci/workspace/tripleo-quickstart-promote-master-delorean-minimal/tripleo-quickstart/roles/libvirt/setup/undercloud/tasks/main.yml:139
Friday 05 August 2016  06:05:24 +0000 (0:02:37.884)       0:06:33.964 ********* 
fatal: [172.19.2.133]: FAILED! => {"changed": true, "cmd": ["virsh", "vol-create-as", "oooq_pool", "undercloud.qcow2", "50G", "--format", "qcow2"], "delta": "0:00:00.160936", "end": "2016-08-05 07:05:25.026677", "failed": true, "rc": 1, "start": "2016-08-05 07:05:24.865741", "stderr": "error: failed to connect to the hypervisor\\nerror: no valid connection\nerror: Failed to connect socket to '/run/user/1000/libvirt/libvirt-sock': Connection refused", "stdout": "", "stdout_lines": [], "warnings": []}

NO MORE HOSTS LEFT *************************************************************

PLAY RECAP *********************************************************************
172.19.2.133               : ok=70   changed=43   unreachable=0    failed=1   
localhost                  : ok=9    changed=4    unreachable=0    failed=0   

'''

RECAP_UNREACHABLE = '''
TASK [tripleo/overcloud : Deploy the overcloud] ********************************
task path: /home/rhos-ci/workspace/tripleo-quickstart-promote-master-delorean-minimal/tripleo-quickstart/roles/tripleo/overcloud/tasks/deploy-overcloud.yml:1
Wednesday 03 August 2016  03:24:53 +0000 (0:00:00.109)       0:36:32.511 ****** 
fatal: [undercloud]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh.", "unreachable": true}

PLAY RECAP *********************************************************************
172.19.2.133               : ok=79   changed=50   unreachable=0    failed=0   
localhost                  : ok=15   changed=7    unreachable=0    failed=0   
undercloud                 : ok=23   changed=16   unreachable=1    failed=0   
'''

MISSING_FILE = '''
+ ansible-playbook -vv /home/centos/workspace/tripleo-quickstart-promote-master-delorean-minimal_pacemaker/playbooks/quickstart.yml -e @/home/centos/workspace/tripleo-quickstart-promote-master-delorean-minimal_pacemaker/config/general_config/minimal_pacemaker.yml -e ansible_python_interpreter=/usr/bin/python -e @/home/centos/workspace/tripleo-quickstart-promote-master-delorean-minimal_pacemaker/config/release/master.yml -e local_working_dir=/home/centos/workspace/tripleo-quickstart-promote-master-delorean-minimal_pacemaker -e virthost=172.19.2.142 -e undercloud_image_url=http://artifacts.ci.centos.org/artifacts/rdo/images/master/delorean/testing/undercloud.qcow2 -t all,teardown-nodes --skip-tags teardown-all,teardown-virthost
Using ./ansible.cfg as config file
ERROR! the file_name '/home/centos/workspace/tripleo-quickstart-promote-master-delorean-minimal_pacemaker/config/general_config/minimal_pacemaker.yml' does not exist, or is not readable
Build step 'Execute shell' marked build as failure
Performing Post build task...
Match found for :Building remotely : True
Logical operation result is TRUE
Running script  : # tripleo-quickstart-cleanup.sh
# A script to cleanup after tripleo-quickstart jobs
# Collects logs and returns the node
set -eux
'''

HUNG_UP = '''
  Cloning https://github.com/redhat-openstack/ansible-role-tripleo-cleanup-nfo.git/ to /tmp/pip-build-7wghkU/ansible-role-tripleo-cleanup-nfo
error: RPC failed; result=7, HTTP code = 0
fatal: The remote end hung up unexpectedly
  Complete output from command git clone -q https://github.com/redhat-openstack/ansible-role-tripleo-cleanup-nfo.git/ /tmp/pip-build-7wghkU/ansible-role-tripleo-cleanup-nfo:
'''

REMOTE_HOST = '''

failed: [172.19.3.114] (item=overcloud-full.tar.md5) => {"cmd": "/usr/bin/rsync --delay-updates -F --compress --archive --rsh 'ssh  -S none -o StrictHostKeyChecking=no' --out-format='<<CHANGED>>%i %n%L' \\"root@172.19.3.114:/var/lib/oooq-images/overcloud-full.tar.md5\\" \\"/home/rhos-ci/workspace/tripleo-quickstart-promote-master-delorean-build-images/images/master/delorean/testing/overcloud-full.tar.md5\\"", "failed": true, "item": "overcloud-full.tar.md5", "msg": "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\\r\\n@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @\\r\\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\\r\\nIT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!\\r\\nSomeone could be eavesdropping on you right now (man-in-the-middle attack)!\\r\\nIt is also possible that a host key has just been changed.\\r\\nThe fingerprint for the ECDSA key sent by the remote host is\\naa:77:ee:0c:c7:ea:dc:5b:cd:d2:56:48:8d:b5:a6:da.\\r\\nPlease contact your system administrator.\\r\\nAdd correct host key in /home/rhos-ci/.ssh/known_hosts to get rid of this message.\\r\\nOffending ECDSA key in /home/rhos-ci/.ssh/known_hosts:242\\r\\nPassword authentication is disabled to avoid man-in-the-middle attacks.\\r\\nKeyboard-interactive authentication is disabled to avoid man-in-the-middle attacks.\\r\\nrsync: link_stat \\"/var/lib/oooq-images/overcloud-full.tar.md5\\" failed: No such file or directory (2)\\nrsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1518) [Receiver=3.0.9]\\n", "rc": 23}

NO MORE HOSTS LEFT *************************************************************

PLAY RECAP *********************************************************************
172.19.3.114               : ok=48   changed=32   unreachable=0    failed=1   
localhost                  : ok=7    changed=3    unreachable=0    failed=0   

'''

SLAVE_OFFLINE = '''
Slave went offline during the build
ERROR: Connection was broken: java.io.IOException: Connection aborted: org.jenkinsci.remoting.nio.NioChannelHub$MonoNioTransport@45bb1345[name=rdo-ci-slave01]
	at org.jenkinsci.remoting.nio.NioChannelHub$NioTransport.abort(NioChannelHub.java:208)
	at org.jenkinsci.remoting.nio.NioChannelHub.run(NioChannelHub.java:629)
	at jenkins.util.ContextResettingExecutorService$1.run(ContextResettingExecutorService.java:28)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
	at java.util.concurrent.FutureTask.run(FutureTask.java:262)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	at java.lang.Thread.run(Thread.java:745)
Caused by: java.io.IOException: Connection timed out
	at sun.nio.ch.FileDispatcherImpl.read0(Native Method)
	at sun.nio.ch.SocketDispatcher.read(SocketDispatcher.java:39)
	at sun.nio.ch.IOUtil.readIntoNativeBuffer(IOUtil.java:223)
	at sun.nio.ch.IOUtil.read(IOUtil.java:197)
	at sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:384)
	at org.jenkinsci.remoting.nio.FifoBuffer$Pointer.receive(FifoBuffer.java:137)
	at org.jenkinsci.remoting.nio.FifoBuffer.receive(FifoBuffer.java:310)
	at org.jenkinsci.remoting.nio.NioChannelHub.run(NioChannelHub.java:561)
	... 6 more

Build step 'Execute shell' marked build as failure
'''

TEMPEST = '''
{1} tempest.scenario.test_volume_boot_pattern.TestVolumeBootPatternV2.test_volume_boot_pattern [204.007266s] ... ok
{1} setUpClass (neutron_vpnaas.tests.tempest.api.test_vpnaas.VPNaaSTestJSON) [0.000000s] ... FAILED
{1} setUpClass (tempest_horizon.tests.scenario.test_dashboard_basic_ops.TestDashboardBasicOps) ... SKIPPED: Horizon support is required
{1} aodh.tests.tempest.api.test_alarming_api.TelemetryAlarmingAPITest.test_alarm_list [0.087036s] ... ok
{1} aodh.tests.tempest.api.test_alarming_api.TelemetryAlarmingAPITest.test_create_delete_alarm_with_combination_rule ... SKIPPED: Skipped until Bug: 1585267 is resolved.
{1} aodh.tests.tempest.api.test_alarming_api.TelemetryAlarmingAPITest.test_create_update_get_delete_alarm [0.527442s] ... ok
{1} aodh.tests.tempest.api.test_alarming_api.TelemetryAlarmingAPITest.test_set_get_alarm_state [0.289299s] ... ok
{1} aodh.tests.tempest.api.test_alarming_api_negative.TelemetryAlarmingNegativeTest.test_get_non_existent_alarm [0.596023s] ... ok
{1} aodh.tests.tempest.api.test_alarming_api_negative.TelemetryAlarmingNegativeTest.test_get_update_show_history_delete_deleted_alarm [0.573877s] ... ok
{1} neutron_fwaas.tests.tempest_plugin.tests.api.test_fwaas_extensions.FWaaSExtensionTestJSON.test_firewall_rule_insertion_position_removal_rule_from_policy [4.462457s] ... ok
'''

PACKSTACK_SUMMARY = '''
Applying 172.19.3.87_compute.pp
\r172.19.3.87_compute.pp:                              [ \u001b[32mDONE\u001b[0m ]
Applying Puppet manifests                            [ \u001b[32mDONE\u001b[0m ]
Finalizing                                           [ \u001b[32mDONE\u001b[0m ]
Running Tempest on 172.19.3.87
Running Tempest                                   [ \u001b[0;31mERROR\u001b[0m ]
'''

if __name__ == "__main__":
    unittest.main()

# test_classify_console.py ends here
