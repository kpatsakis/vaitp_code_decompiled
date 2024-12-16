# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 652_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 626 bytes
import re

def check_for_invalid_imports(template_code):
    if re.search("^\\s*#import\\s+", template_code, re.MULTILINE):
        raise ValueError("Import statements are not allowed in templates.")


try:
    check_for_invalid_imports('\n    # This is a comment\n    #from os import path  # This should not raise an error\n    print("Hello, World!")\n    ')
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 652_1.pyc
