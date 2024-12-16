# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 105_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 677 bytes
import os, shutil

def vulnerable_make_archive(base_name, format, root_dir=None, base_dir=None):
    return shutil.make_archive(base_name, format, root_dir, base_dir)


if __name__ == "__main__":
    user_input_base_name = "../my_archive"
    user_input_format = "zip"
    try:
        vulnerable_make_archive(user_input_base_name, user_input_format, root_dir="/path/to/directory")
        print("Archive created successfully.")
    except Exception as e:
        try:
            print("Error creating archive:", e)
        finally:
            e = None
            del e

# okay decompiling 105_1.pyc
