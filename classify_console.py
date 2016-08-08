#!/usr/bin/env python
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

'''
'''

import re
import sys

recap_regexp = re.compile(
    r'([^\s]+)\s*: ok=(\d+)\s+changed=(\d+)\s+'
    r'unreachable=(\d+)\s+failed=(\d+)')

toplevel_error_regexp = re.compile(
    r"ERROR! the file_name '.*/([^/]+' does not exist, or is not readable)"
)

log_regexp = re.compile(
    r'^fatal:.*?([/a-zA-Z0-9._-]+/([a-zA-Z0-9._-]+)\.log)'
)

error_regexp = re.compile(
    r'^fatal:.*"stderr": "error: ([^\\\\]+)'
    r'|"msg": ".*WARNING: (.*?)[.!].*"'
    r'|"msg": "(.*?)\.?"'
)

generic_regexp = re.compile(
    r'^fatal: (.+)'
    r'|.*(Slave went offline during the build).*'
)

punctuation_regexp = re.compile(r"[':,]")


def first(ll):
    for elt in ll:
        if elt:
            return elt
    return None


def cleanup(data):
    return punctuation_regexp.sub('', data).lower()


def classify(data):
    lines = data.split('\n')
    classified = ('unknown', )
    idx = 0
    for line in lines:
        res = recap_regexp.search(line)
        if res:
            failures = int(res.group(5))
            unreachables = int(res.group(4))
            if failures > 0 or unreachables > 0:
                if res.group(1)[0].isdigit():
                    classified = ('host', )
                else:
                    classified = (res.group(1), )
                break
        res = toplevel_error_regexp.search(line)
        if res:
            classified = ('host', '-'.join(cleanup(res.group(1)).split(' ')))
            break
        idx += 1
    if classified != ('unknown', ):
        while idx >= 0:
            res = log_regexp.search(lines[idx])
            if res:
                classified = (res.group(2), res.group(1))
                break
            else:
                res = error_regexp.search(lines[idx])
                if res:
                    classified = (classified[0],
                                  '-'.join(cleanup(first(res.groups()))
                                           .split(' ')))
                    break
            idx -= 1
    else:
        idx = len(lines) - 1
        while idx >= 0:
            res = generic_regexp.search(lines[idx])
            if res:
                classified = ('host',
                              '-'.join(cleanup(first(res.groups()))
                                       .split(' ')))
                break
            idx -= 1
    return classified

if __name__ == "__main__":
    print ' '.join(classify(sys.stdin.read(-1)))

# classify_console.py ends here
