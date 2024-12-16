# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 716_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 601 bytes
import tensorflow as tf

def vulnerable_poisson_loss(y_true, y_pred):
    return tf.keras.losses.poisson(y_true, y_pred)


y_true = tf.random.uniform((100000, 100000), minval=0, maxval=10)
y_pred = tf.random.uniform((100000, 100000), minval=0, maxval=10)
try:
    loss = vulnerable_poisson_loss(y_true, y_pred)
    print("Loss:", loss.numpy())
except Exception as e:
    try:
        print("Error:", e)
    finally:
        e = None
        del e

# okay decompiling 716_1.pyc
