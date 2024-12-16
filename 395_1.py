# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 395_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 298 bytes
import yaml

def load_model_config(file_path):
    with open(file_path, "r") as file:
        config = yaml.load(file)
    return config


config = load_model_config("model_config.yaml")
print(config)

# okay decompiling 395_1.pyc
