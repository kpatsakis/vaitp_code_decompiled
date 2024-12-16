# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 416_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 299 bytes


def parse_type_line(type_line):
    return eval(type_line)


user_input = "__import__('os').system('ls')"
result = parse_type_line(user_input)

# okay decompiling 416_1.pyc
