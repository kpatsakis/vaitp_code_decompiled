# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 620_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 422 bytes
import tensorflow as tf

def vulnerable_py_func(token):
    return tf.raw_ops.PyFunc(func="your_function", inp=[token], Tout=(tf.float32))


invalid_token = b'\x80\x81'
result = vulnerable_py_func(invalid_token)

# okay decompiling 620_1.pyc
