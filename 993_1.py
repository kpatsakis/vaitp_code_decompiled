# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 993_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 486 bytes
import sys, os

def vulnerable_import(module_name):
    tmp_path = "/tmp"
    if os.path.isdir(tmp_path):
        sys.path.insert(0, tmp_path)
    module = __import__(module_name)
    return module


if __name__ == "__main__":
    module_name = "malicious_module"
    vulnerable_import(module_name)

# okay decompiling 993_1.pyc
