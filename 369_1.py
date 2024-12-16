# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 369_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 412 bytes
import yaml

def load_yaml(yaml_input):
    data = yaml.load(yaml_input)
    return data


malicious_yaml = "\n!!python/object/apply:os.system ['echo Vulnerable!']\n"
load_yaml(malicious_yaml)

# okay decompiling 369_1.pyc
