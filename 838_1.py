# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 838_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 616 bytes
import tensorflow as tf
input_tensor = tf.constant([1, 2, 3], dtype=(tf.qint8))
scale = tf.constant([1.0], dtype=(tf.float32))
offset = tf.constant([0.0], dtype=(tf.float32))
mean = tf.constant([1.0], dtype=(tf.float32))
variance = tf.constant([0.0], dtype=(tf.float32))
result = tf.raw_ops.QuantizedBatchNormWithGlobalNormalization(input=input_tensor,
  scale=scale,
  offset=offset,
  mean=mean,
  variance=variance,
  epsilon=1e-05)
print(result)

# okay decompiling 838_1.pyc
