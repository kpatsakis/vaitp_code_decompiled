# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 2_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 748 bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
cipher = Cipher((algorithms.AES(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')), (modes.CBC(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')), backend=(default_backend()))
encryptor = cipher.encryptor()
immutable_data = b'Hello, World!'
mutable_buffer = bytearray(16)
encryptor.update_into(immutable_data, mutable_buffer)
print(mutable_buffer)
print(immutable_data)

# okay decompiling 2_1.pyc
