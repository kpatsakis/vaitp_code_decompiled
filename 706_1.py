# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 706_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 366 bytes
import tensorflow as tf

@tf.function
def func_a():
    return func_b()


@tf.function
def func_b():
    return func_a()


try:
    func_a()
except RuntimeError as e:
    try:
        print("Caught a RuntimeError, indicating a potential deadlock:", e)
    finally:
        e = None
        del e

else:
    func_a()

# okay decompiling 706_1.pyc
