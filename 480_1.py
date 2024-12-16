# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 480_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 306 bytes
import subprocess

def process_metadata(metadata):
    command = metadata.get("command")
    if command:
        output = subprocess.check_output(command, shell=True)
        return output
    return "No command provided."

# okay decompiling 480_1.pyc
