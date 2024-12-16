# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 775_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 390 bytes
import pyarrow as pa

def create_array_with_nulls(data):
    array = pa.array(data, mask=[value is None for value in data])
    return array


data = [
 1, None, 3, None, 5]
array_with_nulls = create_array_with_nulls(data)
print(array_with_nulls)

# okay decompiling 775_1.pyc
