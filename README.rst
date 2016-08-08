Analyse errors in RDO CI jobs
=============================

RDO CI jobs can be difficult to analyse and this tool is a try to get
some statistics and a first level of analysis.

Here are the jobs this tool is trying to get more clarity about:

https://ci.centos.org/view/rdo/view/promotion-pipeline/

The tool will download only the needed log files on your local system
under the ``jobs`` directory to let you do more analysis if needed.

Usage to analyse one particular job::

 $ ./analyse.sh tripleo-quickstart-promote-master-delorean-minimal 455
 tripleo-quickstart-promote-master-delorean-minimal 455 failure undercloud_post_install introspecting-nodes

This will download the console output of the job in
``jobs/tripleo-quickstart-promote-master-delorean-minimal/455/consoleText``
and it will parse the output to find which log file to analyse
(``/home/stack/undercloud_post_install.log`` in the example). After
downloading the log file from artifact server in
``jobs/tripleo-quickstart-promote-master-delorean-minimal/455/undercloud_post_install.log``,
it will use known patterns to classify the issue (here
``introspecting-nodes``).

For weirdo jobs, it will extract the logs from puppet or packstack
into ``jobs/<jobname>/<jobid>/stderr``.

If you want to analyse the last pipeline, you just have to do::
  
  $ ./get_last_build.sh
  job 591:
    tripleo-quickstart-promote-master-delorean-minimal 459 failure undercloud_post_install unknown-column-unique_key-in-field-list
    tripleo-quickstart-promote-master-delorean-minimal_pacemaker 7 failure undercloud_post_install unknown-column-unique_key-in-field-list
    weirdo-master-promote-packstack-scenario001 455 failure host running-tempest
    weirdo-master-promote-packstack-scenario003 454 failure host running-tempest

It'll display all the jobs in error, it will download the needed log
files and it'll categorize the result according to what has been
discovered with known patterns in the log files.
