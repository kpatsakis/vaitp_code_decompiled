# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 792_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 457 bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def vulnerable_finalize_with_tag(key, iv, ciphertext, tag):
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# okay decompiling 792_1.pyc
