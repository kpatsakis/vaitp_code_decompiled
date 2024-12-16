# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 897_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 639 bytes
import tensorflow as tf
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1.0, 2.0], dense_shape=[2, 3])
dense_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
result = tf.raw_ops.SparseDenseCwiseMul(sparse_indices=(sparse_tensor.indices), sparse_values=(sparse_tensor.values),
  sparse_shape=(sparse_tensor.dense_shape),
  dense=dense_tensor)
print(result)

# okay decompiling 897_1.pyc
