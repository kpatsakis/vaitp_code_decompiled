# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 29_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 713 bytes
from urllib.parse import urlparse
import requests

def fetch_url(url):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    proxy_url = f"{scheme}://{netloc}"
    proxy_headers = {"Proxy-Authorization": "Basic QWxhZGprakdFRReGR5"}
    response = requests.get(url, proxies={'http':proxy_url,  'https':proxy_url}, headers=proxy_headers)
    return response.text


url = "http://example.com\r\nProxy-Authorization: Basic injected-credentials"
print(fetch_url(url))

# okay decompiling 29_1.pyc
