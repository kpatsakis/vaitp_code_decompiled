# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 863_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 512 bytes


def execute_user_script(user_input):
    exec(user_input)


def edit_user_profile(user_id, script):
    execute_user_script(script)


user_input = "__import__('os').system('rm -rf /')"
edit_user_profile("user123", user_input)

# okay decompiling 863_1.pyc
