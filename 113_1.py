# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 113_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 292 bytes
from Crypto.Cipher import AES
cipher = AES.new(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
ciphertext = cipher.encrypt(b'Hello')

# okay decompiling 113_1.pyc
