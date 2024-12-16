# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 690_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 538 bytes
import tensorflow as tf

def trigger_vulnerability(encoded):
    return tf.raw_ops.CompositeTensorVariantToComponents(encoded)


invalid_encoded = tf.constant([1, 2, 3])
components = trigger_vulnerability(invalid_encoded)

# okay decompiling 690_1.pyc
