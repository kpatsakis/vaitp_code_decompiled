# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 17_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 292 bytes
import urllib.parse

def vulnerable_function(url):
    return urllib.parse.urlparse(url).hostname


malicious_url = "xn--" + "a" * 65536 + ".example.com"
try:
    vulnerable_function(malicious_url)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 17_1.pyc
