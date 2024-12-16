# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1046_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 669 bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
private_key = rsa.generate_private_key(public_exponent=65537,
  key_size=1024)
public_key = private_key.public_key()
message = b'Sensitive data'
ciphertext = public_key.encrypt(message, padding.PKCS1v15())
decrypted_message = private_key.decrypt(ciphertext, padding.PKCS1v15())
print(decrypted_message)

# okay decompiling 1046_1.pyc
