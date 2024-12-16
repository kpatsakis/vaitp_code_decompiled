# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 483_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 324 bytes
from pymemcache.client import base
client = base.Client(('localhost', 11211))

def get_data_from_memcache(key):
    data = client.get(key)
    return data


key = "example_key"
data = get_data_from_memcache(key)
print(data)

# okay decompiling 483_1.pyc
