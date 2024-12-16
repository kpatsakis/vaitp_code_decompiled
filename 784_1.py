# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 784_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 524 bytes
import os
from urllib.parse import unquote

def load_script(script_path):
    decoded_path = unquote(script_path)
    script_file_path = decoded_path
    with open(script_file_path, "r") as script_file:
        exec(script_file.read())


load_script("/path/to/libreoffice/share/Scripts/python/../malicious_script.py")

# okay decompiling 784_1.pyc
