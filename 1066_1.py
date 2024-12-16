# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1066_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 347 bytes
array_size = 10
my_array = [0] * array_size

def access_array(index: int):
    return my_array[index]


value = access_array(-1)

# okay decompiling 1066_1.pyc
