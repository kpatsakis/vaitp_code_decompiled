# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 82_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 303 bytes
import typed_ast.ast3 as ast

def parse_python_code(code):
    return ast.parse(code)


malicious_code = "a" * 1000000
try:
    parse_python_code(malicious_code)
except Exception as e:
    try:
        print(f"Error parsing code: {e}")
    finally:
        e = None
        del e

# okay decompiling 82_1.pyc
