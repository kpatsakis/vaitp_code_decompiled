# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 903_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 786 bytes
import tensorflow as tf

def vulnerable_ragged_bincount(splits, values, num_bins):
    batch_idx = 0
    while batch_idx < tf.shape(splits)[0]:
        if splits[batch_idx] == 7:
            break
        batch_idx += 1

    out = tf.zeros([num_bins], dtype=(tf.int32))
    out[-1] += 1
    return out


splits = tf.constant([7])
values = tf.constant([0, 1, 2])
num_bins = 3
output = vulnerable_ragged_bincount(splits, values, num_bins)
print(output)

# okay decompiling 903_1.pyc
