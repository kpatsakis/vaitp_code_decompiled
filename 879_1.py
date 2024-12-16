# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 879_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 393 bytes
import yaml

def load_yaml_model(yaml_string):
    return yaml.unsafe_load(yaml_string)


yaml_model = "\n!<tag:keras.io:layer>\nclass_name: Dense\nconfig:\n  units: 32\n  activation: relu\n"
model_config = load_yaml_model(yaml_model)
print(model_config)

# okay decompiling 879_1.pyc
