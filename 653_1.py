# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 653_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 463 bytes
import tensorflow as tf, pybind11

def to_dlpack(obj):
    tensor_ptr = pybind11.cast(obj)
    return tensor_ptr


vulnerable_output = to_dlpack("not_a_tensor")

# okay decompiling 653_1.pyc
