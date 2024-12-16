# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 819_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 238 bytes
import yaml
with open("untrusted_input.yaml", "r") as file:
    data = yaml.full_load(file)
print(data)

# okay decompiling 819_1.pyc
