# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 812_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 408 bytes
import re

def vulnerable_parse_index_url(url):
    pattern = "^(https?://.*)$"
    match = re.match(pattern, url)
    if match:
        return match.group(0)
    raise ValueError("Invalid index server URL")


try:
    url = "https://example.com/index"
    print(vulnerable_parse_index_url(url))
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 812_1.pyc
