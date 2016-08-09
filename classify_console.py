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
    r'^fatal:.*? > ([/a-zA-Z0-9._-]+/([a-zA-Z0-9._-]+)\.log)'
)

error_regexp = re.compile(
    r'^fatal:.*"stderr": "error: ([^\\\\]+)'
    r'|^(?:fatal|failed):.*"msg": ".*WARNING: (.*?)[.!].*"'
    r'|^(?:fatal|failed):.*"msg": "(.*?)\.?"'
    r'|^fatal:.*"stderr": "(?P<stderr>.*?)", "stdout_lines"'
)

generic_regexp = re.compile(
    r'^fatal: (.+)'
    r'|.*(Slave went offline during the build).*'
)

punctuation_regexp = re.compile(r"['\":,]")

weirdo_regexp = re.compile(
    r'.*\.([\w_.]+).*\[.*\] \.\.\. FAILED'
    r'|^(.*?)\s+\[.*ERROR.*\]$'
)


def first(ll):
    '''return the first non None value'''
    for elt in ll:
        if elt:
            return elt
    return None


def cleanup_result(res):
    if isinstance(res, basestring):
        stri = res
    else:
        stri = first(res.groups())
    return('-'.join(punctuation_regexp.sub('', stri).split(' '))
           .lower())


def classify_stderr(reas, lines):
    '''classify errors from weirdo runs or Python tracebacks'''
    reason = (reas, 'unknown')
    if lines[0] == 'Traceback (most recent call last):':
        return (reason[0], cleanup_result(lines[-1]))
    for idx in xrange(len(lines) - 1, 0, -1):
        res = weirdo_regexp.search(lines[idx])
        if res:
            if res.group(1):
                reason = ('tempest', res.group(1))
            else:
                reason = (reason[0], cleanup_result(res))
            break
    return reason


def classify(data):
    '''classify the console log'''
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
            classified = ('host', cleanup_result(res))
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
                # do not take into account the first fatal error from
                # weirdo jobs as this is only a summary and not the
                # real error. Look for the previous one.
                if (res and res.group(3) !=
                    'A task notified that the playbook execution '
                        'should be failed'):
                    if res.group('stderr'):
                        elines = res.group('stderr').split('\\n')
                        # reformat stderr for better analysis
                        for eline in elines:
                            sys.stderr.write(eline + '\n')
                        classified = classify_stderr(classified[0], elines)
                        break
                    classified = (classified[0], cleanup_result(res))
                    break
            idx -= 1
    else:
        idx = len(lines) - 1
        while idx >= 0:
            res = generic_regexp.search(lines[idx])
            if res:
                classified = ('host', cleanup_result(res))
                break
            idx -= 1
    return classified

if __name__ == "__main__":
    print ' '.join(classify(sys.stdin.read(-1)))

# classify_console.py ends here
