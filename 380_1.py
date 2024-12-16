# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 380_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 385 bytes
import bson

def decode_dbref(dbref):
    return bson.decode_all(bson.BSON.encode(dbref))


invalid_dbref = {'$ref':None, 
 '$id':None}
result = decode_dbref(invalid_dbref)
print(result)

# okay decompiling 380_1.pyc
