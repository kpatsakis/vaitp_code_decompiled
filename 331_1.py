# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 331_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 236 bytes
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
large_message = b'A' * 1000000000
ciphertext = cipher.encrypt(large_message)

# okay decompiling 331_1.pyc
