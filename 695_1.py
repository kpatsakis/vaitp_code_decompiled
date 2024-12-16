# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 695_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 207 bytes
import re

def vulnerable_strip_tags(value):
    while True:
        new_value = re.sub("<[^>]+>", "", value)
        if new_value == value:
            break
        value = new_value

    return value

# okay decompiling 695_1.pyc
