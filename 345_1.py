# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 345_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 550 bytes
from ecdsa import SigningKey, BadSignatureError
sk = SigningKey.generate()
vk = sk.get_verifying_key()
message = b'Important message'
signature = sk.sign(message)
try:
    if vk.verify(signature, message):
        print("Signature is valid!")
    else:
        print("Signature is invalid!")
except BadSignatureError:
    print("Caught a bad signature error!")

# okay decompiling 345_1.pyc
