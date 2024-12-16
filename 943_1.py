# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 943_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 297 bytes
import yaml

def unsafe_load_yaml(yaml_string):
    return yaml.load(yaml_string, Loader=(yaml.Loader))


yaml_data = "\n!!python/object/apply:os.system ['echo Hello, World!']\n"
result = unsafe_load_yaml(yaml_data)

# okay decompiling 943_1.pyc
