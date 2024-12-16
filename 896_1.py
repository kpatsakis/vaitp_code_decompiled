# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 896_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 948 bytes
import tensorflow as tf

def vulnerable_ragged_bincount(splits, values, num_bins):
    splits_values = tf.sparse.to_dense(splits)
    batch_idx = 0
    while batch_idx < tf.shape(splits_values)[0]:
        next_batch_idx = splits_values[batch_idx + 1] if batch_idx + 1 < tf.shape(splits_values)[0] else 0
        batch_idx += 1


splits = tf.SparseTensor(indices=[[0, 0]], values=[0], dense_shape=[1, 1])
values = tf.constant([1])
num_bins = 2
vulnerable_ragged_bincount(splits, values, num_bins)

# okay decompiling 896_1.pyc
