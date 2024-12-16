# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 937_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 474 bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
private_key = RSA.generate(2048)
public_key = private_key.publickey()
message = b'This is a secret message.'
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)

# okay decompiling 937_1.pyc
