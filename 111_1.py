# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 111_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 458 bytes
import urllib3
http = urllib3.PoolManager()
r = http.request("GET", "https://example.com", headers={"Authorization": "Basic YWxhZGRpbjpvcGVuc2VzYW1l"})
r = http.request("GET", "https://example.com/redirect", headers={"Authorization": "Basic YWxhZGRpbjpvcGVuc2VzYW1l"}, redirect=True)

# okay decompiling 111_1.pyc
