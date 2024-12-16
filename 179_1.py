# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 179_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 376 bytes
import hashlib

def hash_data(data):
    hasher = hashlib.sha1()
    hasher.update(data)
    return hasher.hexdigest()


user_input = "large_untrusted_input" * 1000000
print(hash_data(user_input.encode("utf-8")))

# okay decompiling 179_1.pyc
