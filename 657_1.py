# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 657_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 408 bytes
import os

def unsafe_import(module_name):
    module = __import__(module_name)
    return module


if __name__ == "__main__":
    my_module = unsafe_import("my_module")

# okay decompiling 657_1.pyc
