# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 464_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 370 bytes
import os

def save_file(user_input_path, data):
    with open(user_input_path, "w") as file:
        file.write(data)


user_input = "/path/to/user/specified/file.txt"
data_to_save = "Sensitive data"
save_file(user_input, data_to_save)

# okay decompiling 464_1.pyc
