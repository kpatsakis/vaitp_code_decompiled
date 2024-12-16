# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 825_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 429 bytes
import os, ctypes

def load_python_dll():
    dll_path = "C:\\DLLs\\python3.dll"
    if os.path.exists(dll_path):
        ctypes.WinDLL(dll_path)
    else:
        raise FileNotFoundError("The specified DLL does not exist.")


load_python_dll()

# okay decompiling 825_1.pyc
