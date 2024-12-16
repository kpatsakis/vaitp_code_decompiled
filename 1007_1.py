# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1007_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 386 bytes
import requests

def vulnerable_request(url):
    response = requests.get(url)
    exec(response.text)
    return response.json()


data = vulnerable_request("https://api.example.com/data")
if data:
    print(data)

# okay decompiling 1007_1.pyc
