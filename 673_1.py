# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 673_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 255 bytes
import os

def execute_command(command):
    result = os.system(command)
    return result


user_command = input("Enter a command to execute: ")
execute_command(user_command)

# okay decompiling 673_1.pyc
