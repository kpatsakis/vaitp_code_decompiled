# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1048_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 406 bytes


def is_in_or_equal(directory, target):
    return target.startswith(directory)


directory = "/safe/directory"
target_file = "/safe/directory/../restricted_file.txt"
if is_in_or_equal(directory, target_file):
    print("Access granted to:", target_file)
else:
    print("Access denied to:", target_file)

# okay decompiling 1048_1.pyc
