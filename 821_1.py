# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 821_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 384 bytes
import tensorflow as tf

def create_ragged_tensor(values, row_splits):
    return tf.ragged.constant(values, row_splits=row_splits)


ragged_tensor = create_ragged_tensor([[1, 2], [3] * 1000000], [0, 2, 2])
print(ragged_tensor)

# okay decompiling 821_1.pyc
