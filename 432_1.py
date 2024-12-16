# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 432_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 151 bytes


def vulnerable_function(input_string):
    if input_string == "expected_value":
        return True
    return False

# okay decompiling 432_1.pyc
