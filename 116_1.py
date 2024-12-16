# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 116_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 330 bytes
import difflib

def compare_lines(line1, line2):
    return difflib.IS_LINE_JUNK(line1) or difflib.IS_LINE_JUNK(line2)


compare_lines("a" * 50000, "b" * 50000)

# okay decompiling 116_1.pyc
