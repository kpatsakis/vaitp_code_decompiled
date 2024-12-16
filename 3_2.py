# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 3_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 613 bytes
from os import path
user_input_path = "/legitimate/path\x00/../../../../etc/passwd"
normalized_path = path.normpath(user_input_path)
print("Normalized Path:", normalized_path)

# okay decompiling 3_2.pyc
