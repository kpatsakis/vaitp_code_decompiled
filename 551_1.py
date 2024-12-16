# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 551_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 418 bytes
import tempfile

def insecure_temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    return temp_file.name


temp_file_path = insecure_temp_file()
with open(temp_file_path, "w") as f:
    f.write("Insecure temporary file content.")

# okay decompiling 551_1.pyc
