# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 726_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 278 bytes
import os, ctypes

def load_library(library_name):
    return ctypes.CDLL(library_name)


try:
    my_library = load_library("my_library.dll")
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 726_1.pyc
