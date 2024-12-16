# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 56_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 324 bytes
import ctypes

def vulnerable_function(user_input):
    obj = ctypes.c_double(user_input)
    repr(obj)


user_input = "1.23456789012345678901234567890"
vulnerable_function(user_input)

# okay decompiling 56_1.pyc
