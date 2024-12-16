# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 421_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 294 bytes
import re

def encode_structured_data(data):
    pattern = "^0x[a-fA-F0-9]{40}$"
    if not re.match(pattern, data):
        raise ValueError("Invalid input format")
    return "Encoded data"

# okay decompiling 421_1.pyc
