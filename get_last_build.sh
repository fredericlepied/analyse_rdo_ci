#!/bin/bash
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

json=json.$$

jname=$1
jbid=$2

if [ -z "$jname" ]; then
    jname=rdo-delorean-promote-master
fi

if [ -z "$jbid" ]; then
    jbid=lastBuild
fi

curl --fail -s -o $json https://ci.centos.org/view/rdo/view/promotion-pipeline/job/$jname/$jbid/api/json

global_result=$(jq -r .result $json)

if [ $global_result = FAILURE ]; then
    echo "job $(jq -r .id $json):"
    len=$(jq '.subBuilds | length' $json)

    for idx in $(seq 0 $(($len - 1))); do
        result=$(jq -r ".subBuilds[$idx].result" $json)
        case $result in
            FAILURE)
                bn=$(jq -r ".subBuilds[$idx].buildNumber" $json)
                jn=$(jq -r ".subBuilds[$idx].jobName" $json)
                echo -n "    "
                $(dirname $0)/analyse.sh $jn $bn
                ;;
        esac
    done|sort
else
    echo "nothing to analyse ($global_result)" 1>&2
fi

rm $json

# get_last_build.sh ends here
