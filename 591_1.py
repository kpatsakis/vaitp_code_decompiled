# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 591_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 518 bytes
import os
script_directory = "/path/to/spss/scripts"

def set_weak_permissions(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.chmod(file_path, 438)


set_weak_permissions(script_directory)

# okay decompiling 591_1.pyc
