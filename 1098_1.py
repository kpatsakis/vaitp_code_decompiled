# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1098_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 329 bytes
import yaml

def load_yaml_unsafe(file_path):
    with open(file_path, "r") as file:
        data = yaml.load(file, Loader=(yaml.FullLoader))
    return data


data = load_yaml_unsafe("example.yaml")
print(data)

# okay decompiling 1098_1.pyc
