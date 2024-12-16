# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 186_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 321 bytes
import hashlib

def generate_hash_with_salt(user_input):
    salt = "fixed_salt"
    data_to_hash = salt + user_input
    return hashlib.sha1(data_to_hash.encode()).hexdigest()


user_input = "sensitive_data"
print(generate_hash_with_salt(user_input))

# okay decompiling 186_1.pyc
