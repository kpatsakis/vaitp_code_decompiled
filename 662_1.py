# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 662_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 653 bytes
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
quantized_tensor = tf.compat.v1.quantize((tf.constant([1.0, 2.0])), min_range=0.0, max_range=3.0, T=(tf.quint8))
print(quantized_tensor)

# okay decompiling 662_1.pyc
