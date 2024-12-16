# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 671_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 306 bytes
import re

def validate(input_string):
    pattern = "(.+?)\\((.*)\\)"
    if re.match(pattern, input_string):
        return True
    return False


print(validate("valid_input(param)"))
print(validate("invalid_input("))

# okay decompiling 671_1.pyc
