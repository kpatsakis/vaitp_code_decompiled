# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1157_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 266 bytes


def unsafe_file_write(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


unsafe_file_write("/path/to/executable.py", 'print("Malicious code execution")')

# okay decompiling 1157_1.pyc
