# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 528_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 305 bytes
import yaml

def load_yaml(yaml_string):
    return yaml.load(yaml_string)


yaml_data = "\n!!python/object/apply:os.system ['echo Vulnerable']\n"
data = load_yaml(yaml_data)
print(data)

# okay decompiling 528_1.pyc
