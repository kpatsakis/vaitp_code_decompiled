# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 39_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 695 bytes
import urllib3
http = urllib3.PoolManager()
proxy = "https://malicious.com:8080"
url = "https://example.com"
response = http.request("GET", url, retries=False, timeout=10, preload_content=False, proxy_url=proxy)

# okay decompiling 39_2.pyc
