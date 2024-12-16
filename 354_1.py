# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 354_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 542 bytes
from ecdsa import VerifyingKey, BadSignatureError
public_key = "-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----"
malformed_signature = b'malformed_signature_data'
vk = VerifyingKey.from_pem(public_key)
try:
    vk.verify(malformed_signature, b'message')
except BadSignatureError:
    print("Signature verification failed.")
except Exception as e:
    try:
        print(f"An unexpected error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 354_1.pyc
