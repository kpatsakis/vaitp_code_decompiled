# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 32_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 330 bytes
import urllib3

def fetch_url(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    return response.data


url = "http://example.com@" * 1000
try:
    data = fetch_url(url)
    print(data)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 32_1.pyc
