# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 470_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 444 bytes
import sys

def handle_core_dump(module_name):
    try:
        __import__(module_name)
    except ImportError as e:
        try:
            print(f"Error importing module: {e}")
        finally:
            e = None
            del e


user_input = sys.argv[1]
handle_core_dump(user_input)

# okay decompiling 470_1.pyc
