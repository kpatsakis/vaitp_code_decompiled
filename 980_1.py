# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 980_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 801 bytes
import os, ctypes

def vulnerable_dll_load():
    dll_name = "wlbsctrl.dll"
    untrusted_path = "C:\\Python27\\Scripts"
    try:
        dll_path = os.path.join(untrusted_path, dll_name)
        ctypes.WinDLL(dll_path)
        print(f"Successfully loaded {dll_name} from {untrusted_path}")
    except Exception as e:
        try:
            print(f"Failed to load {dll_name}: {e}")
        finally:
            e = None
            del e


vulnerable_dll_load()

# okay decompiling 980_1.pyc
