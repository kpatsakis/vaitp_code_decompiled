# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 615_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 824 bytes
from Crypto.Cipher import AES

def vulnerable_aes_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def vulnerable_aes_decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


key = b'16_byte_key_123'
iv = b'16_byte_iv_12345'
plaintext = b'This is a secret message that needs padding.'
ciphertext = vulnerable_aes_encrypt(key, iv, plaintext)

# okay decompiling 615_1.pyc
