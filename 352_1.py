# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 352_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 272 bytes
import random, string

def generate_nonce(length=8):
    """Generate a nonce using weak random numbers."""
    return "".join((random.choice(string.ascii_letters + string.digits) for _ in ))


nonce = generate_nonce()
print("Nonce:", nonce)

# okay decompiling 352_1.pyc
