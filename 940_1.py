# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 940_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 517 bytes
import os, shutil, tempfile

def vulnerable_rmtree(path):
    shutil.rmtree(path)


try:
    temp_dir = tempfile.gettempdir()
    os.mkdir(os.path.join(temp_dir, "to_delete"))
    vulnerable_rmtree(os.path.join(temp_dir, "to_delete"))
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 940_1.pyc
