# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 581_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 215 bytes


def execute_command(command):
    return eval(command)


user_input = "os.system('ls')"
execute_command(user_input)

# okay decompiling 581_1.pyc
