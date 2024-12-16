# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 506_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 554 bytes
import sys
module_name = "malicious"
try:
    imported_module = __import__(module_name)
except ImportError as e:
    try:
        print(f"Error importing module: {e}")
    finally:
        e = None
        del e

# okay decompiling 506_1.pyc
