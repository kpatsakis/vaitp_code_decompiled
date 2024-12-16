# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 785_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 518 bytes
import re

def vulnerable_parse(input_string):
    pattern = re.compile("^(.*)([a-zA-Z0-9_]+)(.*)$")
    if pattern.match(input_string):
        return True
    raise ValueError("Input string is not valid.")


try:
    result = vulnerable_parse("a" * 10000 + "valid_input" + "b" * 10000)
    print("Input is valid:", result)
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 785_1.pyc
