# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 214_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 291 bytes
import os

def create_temp_file():
    temp_file = "/tmp/temp_file"
    os._execvpe("touch", ("touch", temp_file), {})
    return temp_file


temp_file = create_temp_file()
os.remove(temp_file)

# okay decompiling 214_1.pyc
