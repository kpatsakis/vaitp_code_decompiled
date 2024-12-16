# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 170_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 245 bytes
import hashlib

def insecure_hash_function(user_input):
    return hashlib.sha256(user_input.encode()).hexdigest()


print(insecure_hash_function("example"))

# okay decompiling 170_1.pyc
