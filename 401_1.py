# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 401_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 388 bytes
state = {"value": 0}

def side_effect_function():
    state["value"] += 1
    return state["value"]


result = unsafe_add(5, side_effect_function())
print(result)

# okay decompiling 401_1.pyc
