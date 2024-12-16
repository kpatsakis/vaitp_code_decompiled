# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 448_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 354 bytes
import ujson

def unsafe_encode(data, indent):
    return ujson.dumps(data, indent=indent)


data = {"key": "value"}
encoded_data = unsafe_encode(data, indent=1000)
print(encoded_data)

# okay decompiling 448_1.pyc
