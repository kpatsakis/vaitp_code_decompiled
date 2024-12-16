# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 192_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 451 bytes
import audioop

def vulnerable_lin2lin(data, nchannels, width, new_nchannels, new_width):
    return audioop.lin2lin(data, width, new_width, new_nchannels)


large_data = b'\x00' * 2147483648
result = vulnerable_lin2lin(large_data, 1, 2, 2, 2)

# okay decompiling 192_1.pyc
