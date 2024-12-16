# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 61_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 504 bytes
import urllib3

def vulnerable_function(url, headers):
    http = urllib3.PoolManager()
    request = http.request("GET", url, headers=headers)
    return request.data


url = "https://example.com"
headers = {'Transfer-Encoding':"chunked", 
 'Content-Length':"0"}
chunked_payload = "5\r\nHello\r\n0\r\n\r\n"
vulnerable_function(url, headers)
http = urllib3.PoolManager()
request = http.request("POST", url, body=chunked_payload)

# okay decompiling 61_1.pyc
