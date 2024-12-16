# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 468_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 343 bytes
import os

def create_temp_file():
    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, "w") as temp_file:
        temp_file.write("This is a temporary file.")
    return temp_file_path


temp_file = create_temp_file()
print(f"Temporary file created at: {temp_file}")

# okay decompiling 468_1.pyc
