# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1181_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 532 bytes
import urllib3
http = urllib3.PoolManager()
headers = {"Proxy-Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="}
response = http.request("GET", "http://example.com", headers=headers)
print(response.data)

# okay decompiling 1181_1.pyc
