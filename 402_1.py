# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 402_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 406 bytes


def vulnerable_function(a, b):
    global side_effect_var
    side_effect_var = a + 1
    return uint256_addmod(a, side_effect_var, 10)

# okay decompiling 402_1.pyc
