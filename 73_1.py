# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 73_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 545 bytes
import urllib.request

def non_vulnerable_function(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    content = response.read().decode("utf-8")
    if "a" in content or "b" in content:
        print("Pattern found")
    else:
        print("Pattern not found")


url = "http://example.com/valid-content"
non_vulnerable_function(url)

# okay decompiling 73_1.pyc
