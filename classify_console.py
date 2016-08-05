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
    '([^\s]+)\s*: ok=(\d+)\s+changed=(\d+)\s+'
    'unreachable=(\d+)\s+failed=(\d+)')

log_regexp = re.compile(
    '^fatal:.*?([/a-zA-Z0-9._-]+/([a-zA-Z0-9._-]+)\.log)'
)

error_regexp = re.compile(
    '^fatal:.*"stderr": "error: ([^\\\\]+)'
    '|"msg": "(.*?)\.?"'
)


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
                                  '-'.join((res.group(1) or
                                            res.group(2)).lower().split(' ')))
                    break
            idx -= 1
    return classified

if __name__ == "__main__":
    print ' '.join(classify(sys.stdin.read(-1)))

# classify_console.py ends here
