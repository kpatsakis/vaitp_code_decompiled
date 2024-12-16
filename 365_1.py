# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 365_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 211 bytes
import urllib.request

def fetch_data(url):
    response = urllib.request.urlopen(url)
    return response.read()


data = fetch_data("https://example.com/api")
print(data)

# okay decompiling 365_1.pyc
