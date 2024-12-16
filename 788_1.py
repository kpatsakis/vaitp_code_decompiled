# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 788_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 590 bytes
import requests

class PKIConnection:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, verify=False)
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, verify=False)
        return response

# okay decompiling 788_1.pyc
