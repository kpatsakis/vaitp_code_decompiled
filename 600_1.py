# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 600_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 233 bytes


def unsafe_script_invoke(script):
    exec(script)


user_input_script = "__import__('os').system('ls')"
unsafe_script_invoke(user_input_script)

# okay decompiling 600_1.pyc
