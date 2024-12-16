# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 93_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 339 bytes
import urllib3
ssl_context = urllib3.ssl_.create_urllib3_ssl_context()
pool_manager = urllib3.PoolManager.ssl_context = ssl_context
response = pool_manager.request("GET", "https://self-signed-server.com")
print(response.status)

# okay decompiling 93_1.pyc
