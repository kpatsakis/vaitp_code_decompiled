# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 110_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 353 bytes
import pickle
payload = b'\x80\x04\x95\x08\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x08test_func\x94\x93\x94.\xff\xff\xff\xff'
obj = pickle.loads(payload)
print(obj)

# okay decompiling 110_1.pyc
