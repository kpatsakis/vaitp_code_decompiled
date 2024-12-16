# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 493_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 579 bytes
import os, sys
print("Current working directory:", os.getcwd())
sys.path.append(os.getcwd())
try:
    import some_module
except ImportError as e:
    try:
        print("Import failed:", e)
    finally:
        e = None
        del e

# okay decompiling 493_1.pyc
