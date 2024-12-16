# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 346_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 502 bytes
import rsa
public_key, private_key = rsa.newkeys(512)
message = b'Secret Message'
ciphertext = rsa.encrypt(message, public_key)
malicious_ciphertext = b'\x00' + ciphertext
try:
    decrypted_message = rsa.decrypt(malicious_ciphertext, private_key)
    print("Decrypted message:", decrypted_message)
except rsa.DecryptionError:
    print("Decryption failed.")

# okay decompiling 346_1.pyc
