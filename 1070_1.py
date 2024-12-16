# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1070_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1030 bytes
from deepdiff import Delta

def vulnerable_deserialize(delta_serialized):
    delta = Delta.from_dict(delta_serialized)
    return delta


delta_serialized = {'some_attribute':"new_value", 
 '__dunder_attribute__':"malicious_value"}
vulnerable_delta = vulnerable_deserialize(delta_serialized)

class Target:

    def __init__(self):
        self.some_attribute = "original_value"
        self.__dunder_attribute__ = "original_dunder_value"


target_instance = Target()
print("Before:", target_instance.some_attribute, target_instance.__dunder_attribute__)
for key, value in vulnerable_delta.items():
    setattr(target_instance, key, value)
else:
    print("After:", target_instance.some_attribute, target_instance.__dunder_attribute__)

# okay decompiling 1070_1.pyc
