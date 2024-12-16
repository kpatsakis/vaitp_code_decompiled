# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 200_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 471 bytes


def vulnerable_integer_addition(a, b):
    return a + b


def vulnerable_integer_multiplication(a, b):
    return a * b


result_add = vulnerable_integer_addition(2147483647, 1)
print(result_add)
result_mul = vulnerable_integer_multiplication(100000, 30000)
print(result_mul)

# okay decompiling 200_1.pyc
