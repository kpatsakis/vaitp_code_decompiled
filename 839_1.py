# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 839_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 942 bytes
import tensorflow as tf

def vulnerable_sdca_optimizer(learning_rate, num_iterations):
    optimizer = tf.raw_ops.SdcaOptimizer(learning_rate=learning_rate,
      num_iterations=num_iterations,
      dual_coefficients=None,
      primal_loss=None)
    return optimizer


result = vulnerable_sdca_optimizer(0.01, 100)

# okay decompiling 839_1.pyc
