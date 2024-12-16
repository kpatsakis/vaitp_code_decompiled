# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 616_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 636 bytes
import re

def normalize_url(url):
    pattern = "^(https?://)?(www\\.)?([a-zA-Z0-9.-]+)(/.*)?$"
    match = re.match(pattern, url)
    if match:
        scheme = match.group(1) or "http://"
        domain = match.group(3)
        path = match.group(4) or "/"
        return f"{scheme}{domain}{path}"
    raise ValueError("Invalid URL")


try:
    print(normalize_url("http://example.com/" + "a" * 10000 + "/path"))
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 616_1.pyc
