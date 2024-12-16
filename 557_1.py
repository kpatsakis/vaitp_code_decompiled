# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 557_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 800 bytes
from Cryptodome.Cipher import AES

class InsecureEncryption:

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_data = self._pad(data)
        encrypted_data = cipher.encrypt(padded_data)
        return encrypted_data

    def _pad(self, data):
        pad_len = AES.block_size - len(data) % AES.block_size
        return data + bytes([pad_len] * pad_len)


key = b'Sixteen byte key'
iv = b'Sixteen byte iv.'
insecure_encryption = InsecureEncryption(key, iv)
encrypted = insecure_encryption.encrypt(b'Secret Message')

# okay decompiling 557_1.pyc
