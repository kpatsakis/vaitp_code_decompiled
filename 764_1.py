# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 764_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 339 bytes
import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


password = input("Enter your password: ")
hashed = hash_password(password)
print("Password hashed successfully.")

# okay decompiling 764_1.pyc
