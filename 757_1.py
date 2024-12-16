# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 757_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 254 bytes


def vulnerable_open(file_path, mode):
    return open(file_path, mode)


with vulnerable_open("/some_arbitrary_path/my_file.txt", "w") as f:
    f.write("This could be any file!")

# okay decompiling 757_1.pyc
