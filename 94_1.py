# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 94_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 693 bytes
import urllib3
url = "http://example.com\r\nX-Fake-Header: injected\r\n\r\n"
http_connection = urllib3.PoolManager()
try:
    response = http_connection.request("GET", url)
    if "X-Fake-Header" in response.headers:
        print("The response contains a CRLF injection")
    else:
        print("The response does not contain a CRLF injection")
except Exception as e:
    try:
        print("An error occurred:", e)
    finally:
        e = None
        del e

# okay decompiling 94_1.pyc
