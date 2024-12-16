# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 664_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 359 bytes
import sys

def vulnerable_import(module_name):
    sys.path.append("")
    __import__(module_name)


vulnerable_import("malicious_module")

# okay decompiling 664_1.pyc
