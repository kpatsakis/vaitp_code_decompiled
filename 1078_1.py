# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1078_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 499 bytes
import pymongo
from bson import BSON
malicious_data = b'\x16\x00\x00\x00\x02name\x00\x05\x00\x00\x00Alice\x00\x00\xff\xff\xff'
try:
    document = BSON(malicious_data).decode()
    print(document)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 1078_1.pyc
