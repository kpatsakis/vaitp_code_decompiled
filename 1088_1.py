# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1088_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 480 bytes
from pymongo import MongoClient
from bson import BSON
client = MongoClient("mongodb://localhost:27017/")
db = client.test_database
malformed_bson = b'\x00\x01\x02'
data = BSON(malformed_bson).decode()
print(data)

# okay decompiling 1088_1.pyc
