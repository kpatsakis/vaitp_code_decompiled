# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 859_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 604 bytes
import numpy as np
try:
    dimensions = tuple([2] * 33)
    large_dim_array = np.zeros(dimensions)
    print("Array created successfully:", large_dim_array.shape)
except Exception as e:
    try:
        print("Error occurred:", e)
    finally:
        e = None
        del e

# okay decompiling 859_1.pyc
