# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 624_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 391 bytes
import pickle

def renderLocalView(data):
    try:
        deserialized_data = pickle.loads(data)
        return         return process_data(deserialized_data)
    except Exception as e:
        try:
            raise ValueError("Error processing data: {}".format(e))
        finally:
            e = None
            del e

# okay decompiling 624_1.pyc
