# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 987_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 344 bytes
import subprocess

def execute_command(command):
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout


user_input = "ls -l; rm -rf /"
output = execute_command(user_input)
print(output)

# okay decompiling 987_1.pyc
