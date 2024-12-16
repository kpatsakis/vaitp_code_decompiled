# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 693_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 367 bytes
import pickle

def load_data(serialized_data):
    return pickle.loads(serialized_data)


def process_data(serialized_data):
    try:
        data = load_data(serialized_data)
    except Exception as e:
        try:
            print(f"Error processing data: {e}")
        finally:
            e = None
            del e

# okay decompiling 693_1.pyc
