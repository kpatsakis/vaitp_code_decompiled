# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 478_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 224 bytes
import subprocess

def execute_command(command):
    subprocess.Popen(command, shell=True)


user_input = input("Enter a command to execute: ")
execute_command(user_input)

# okay decompiling 478_1.pyc
