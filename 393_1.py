# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 393_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 530 bytes
import rsa

def decrypt_message(private_key, ciphertext):
    decrypted_message = rsa.decrypt(ciphertext, private_key)
    return decrypted_message


private_key, public_key = rsa.newkeys(512)
ciphertext = rsa.encrypt(b'Secret Message', public_key)
try:
    plaintext = decrypt_message(private_key, ciphertext)
    print(plaintext.decode())
except rsa.DecryptionError:
    print("Decryption failed.")

# okay decompiling 393_1.pyc
