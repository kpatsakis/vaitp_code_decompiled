# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 51_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 921 bytes
import urllib.parse
proxy_url = "http://example.com/cache"
url = "http://example.com/app?param1=value1;param2=value2"
proxy_handler = urllib.request.ProxyHandler({"http": proxy_url})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
print(response.read().decode())

# okay decompiling 51_1.pyc
