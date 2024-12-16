# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 962_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 279 bytes
import random

def generate_one_time_code(length=6):
    """Generate a weak one-time code using random module."""
    return "".join(random.choices("0123456789", k=length))


one_time_code = generate_one_time_code()
print(f"Your one-time code is: {one_time_code}")

# okay decompiling 962_1.pyc
