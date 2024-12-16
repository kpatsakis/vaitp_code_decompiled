# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 836_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 347 bytes
import requests

def make_request_to_domain(domain):
    response = requests.get(domain)
    return response.content


domain = "http://example.com"
make_request_to_domain(domain)

# okay decompiling 836_1.pyc
