# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 963_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 727 bytes
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def get_key(secret: str) -> bytes:
    return hashlib.md5(secret.encode()).digest()


def encrypt(plaintext: str, secret: str) -> bytes:
    key = get_key(secret)
    cipher = AES.new(key, (AES.MODE_CBC), iv=(b'0' * AES.block_size))
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext


secret_key = "my_secret"
message = "This is a secret message."
encrypted_message = encrypt(message, secret_key)
print(encrypted_message.hex())

# okay decompiling 963_1.pyc
