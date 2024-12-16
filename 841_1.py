# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 841_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 383 bytes
import tensorflow as tf

def load_model(model_path):
    model = tf.saved_model.load(model_path)
    mlir_ir = tf.experimental.mlir.convert_to_mlir(model)
    return mlir_ir


model_path = "path/to/saved_model"
mlir_ir = load_model(model_path)

# okay decompiling 841_1.pyc
