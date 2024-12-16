# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1010_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 512 bytes


@public
def vulnerable_function(arg1, arg2=10, arg3=20):
    return arg1 + arg2 + arg3


result = vulnerable_function(5)

# okay decompiling 1010_1.pyc
