# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 197_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 371 bytes


def vulnerable_expandtabs(input_string, tabsize):
    return input_string.expandtabs(tabsize)


result = vulnerable_expandtabs("Hello\tWorld", 2147483648)
print(result)

# okay decompiling 197_1.pyc
