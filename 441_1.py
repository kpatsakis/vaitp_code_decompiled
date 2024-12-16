# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 441_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 328 bytes
import os
secret_file_path = "secret.txt"
with open(secret_file_path, "w") as secret_file:
    secret_file.write("API_KEY=your_api_key_here")
os.chmod(secret_file_path, 438)

# okay decompiling 441_1.pyc
