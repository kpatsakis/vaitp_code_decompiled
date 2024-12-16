# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 23_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 583 bytes
import os, sys

def add_user_writable_path():
    user_writable_directory = "C:\\Users\\Public\\WritableDirectory"
    current_path = os.environ.get("PATH", "")
    new_path = current_path + os.pathsep + user_writable_directory
    os.environ["PATH"] = new_path


if __name__ == "__main__":
    add_user_writable_path()
    print("Insecure PATH modified:", os.environ["PATH"])

# okay decompiling 23_1.pyc
