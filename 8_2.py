# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 8_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 457 bytes
import requests
proxy_url = "http://user:pass@proxy.example.com:8080"
proxy_dict = {'http':proxy_url,  'https':proxy_url}
target_url = "http://example.com"
response = requests.get(target_url, proxies=proxy_dict)
print(response.status_code)
print(response.text)

# okay decompiling 8_2.pyc
