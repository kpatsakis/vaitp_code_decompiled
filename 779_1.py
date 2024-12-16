# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 779_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 702 bytes


def vulnerable_mget(input_string):
    pointer = None
    if len(input_string) > 100:
        pointer = input_string[100[:None]]
    processed_string = input_string + pointer
    return processed_string


result = vulnerable_mget("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(result)

# okay decompiling 779_1.pyc
