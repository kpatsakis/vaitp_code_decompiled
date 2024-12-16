# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 881_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 249 bytes


def execute_macro(user_input):
    eval(user_input)


user_input = "print('This is a malicious command!')"
execute_macro(user_input)

# okay decompiling 881_1.pyc
