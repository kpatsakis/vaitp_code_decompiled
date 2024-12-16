# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1019_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 478 bytes
import os

def load_idb_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("The specified IDB file does not exist.")
    print(f"Loading IDB file: {file_path}")
    exec(open(file_path).read())


try:
    load_idb_file("example.idb")
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 1019_1.pyc
