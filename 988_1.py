# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 988_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 299 bytes
from ecdsa import SigningKey, NIST256p
sk = SigningKey.generate(curve=NIST256p)
vk = sk.verifying_key
message = b'Secure message'
signature = sk.sign(message)
assert vk.verify(signature, message)
print("Signature verified.")

# okay decompiling 988_1.pyc
