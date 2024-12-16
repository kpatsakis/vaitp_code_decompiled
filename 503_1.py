# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 503_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 796 bytes
import os, sys

def vulnerable_function():
    os.environ["PYTHONPATH"] = "/untrusted/directory"
    try:
        import trusted_module
    except ImportError:
        print("Could not import the trusted module.")


if __name__ == "__main__":
    vulnerable_function()

# okay decompiling 503_1.pyc
