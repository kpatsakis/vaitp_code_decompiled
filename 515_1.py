# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 515_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 250 bytes
import pickle

def vulnerable_load(data):
    return pickle.loads(data)


data = b'...'
obj = vulnerable_load(data)

# okay decompiling 515_1.pyc
