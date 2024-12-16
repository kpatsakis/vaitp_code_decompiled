# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 490_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 494 bytes
import os, sys

def vulnerable_import(module_name):
    current_dir = os.getcwd()
    sys.path.append(current_dir)
    __import__(module_name)


if __name__ == "__main__":
    vulnerable_import("some_module")

# okay decompiling 490_1.pyc
