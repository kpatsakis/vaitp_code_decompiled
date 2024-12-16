# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1068_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 284 bytes
import requests

def save_url_to_cache(path):
    response = requests.get(path)


save_url_to_cache("http://169.254.169.254/latest/meta-data/")

# okay decompiling 1068_1.pyc
