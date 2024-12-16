# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 610_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 260 bytes
import pickle, os

def load_pickle(file_path):
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    return data

# okay decompiling 610_1.pyc
