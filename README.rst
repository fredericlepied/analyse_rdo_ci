Analyse errors in RDO CI jobs
=============================

Usage::

 $ ./analyse.sh tripleo-quickstart-promote-master-delorean-minimal 455
 tripleo-quickstart-promote-master-delorean-minimal 455 failure undercloud_post_install introspecting-nodes

This will download the console output of the job in
`jobs/tripleo-quickstart-promote-master-delorean-minimal/455/consoleText`
and it will parse the output to find which log file to analyse
(`/home/stack/undercloud_post_install.log` in the example). After
downloading the log file from artifact server in
`jobs/tripleo-quickstart-promote-master-delorean-minimal/455/undercloud_post_install.log`,
it will use known patterns to classify the issue (here
`introspecting-nodes`).
