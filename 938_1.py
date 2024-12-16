# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 938_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 329 bytes
import math

def calculate_storage_slots(size_in_bytes):
    return math.ceil(size_in_bytes / 32)


size_in_bytes = 70368744177663
slots_needed = calculate_storage_slots(size_in_bytes)
print(slots_needed)

# okay decompiling 938_1.pyc
