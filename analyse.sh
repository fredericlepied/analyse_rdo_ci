#!/bin/sh
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

jobname="$1"
jobid="$2"

job="$jobname/$jobid"

mkdir -p jobs/"$job"

if [ ! -r jobs/"$job"/json ]; then
    curl --fail -s https://ci.centos.org/view/rdo/view/promotion-pipeline/job/"$job"/api/json > jobs/"$job"/json
    if [ $? != 0 ]; then
        rm -rf jobs/"$job"
        exit 1
    fi
fi

# only download log from failed jobs
case $(jq . jobs/"$job"/json | grep '^  "result"') in
    *FAILURE*)
        if [ ! -r jobs/"$job"/consoleText ]; then
            curl -s -o jobs/"$job"/consoleText https://ci.centos.org/job/$job/consoleText
        fi
        echo -n "$jobname $jobid "
        result=$(./classify.py < jobs/"$job"/consoleText)
        echo "$result"
        ;;
    *)
        echo "$jobname $jobid success"
esac

# analyse.sh ends here
