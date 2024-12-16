# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 800_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1025 bytes
import tensorflow as tf

def vulnerable_transposed_convolution(input_shape, filters, kernel_size):
    model = tf.keras.Sequential([
     tf.keras.layers.Input(shape=input_shape),
     tf.keras.layers.Conv2DTranspose(filters, kernel_size, padding="same", activation="relu")])
    quantized_model = tf.quantization.quantize(model, input_quantization=(tf.quantization.quantize_weights),
      output_quantization=(tf.quantization.quantize_weights))
    return quantized_model


input_shape = (32, 32, 3)
filters = 16
kernel_size = (3, 3)
vulnerable_model = vulnerable_transposed_convolution(input_shape, filters, kernel_size)

# okay decompiling 800_1.pyc
