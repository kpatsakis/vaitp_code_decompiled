# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1109_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 878 bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=(default_backend()))
mismatched_public_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=(default_backend())).public_key()
from cryptography.hazmat.primitives.serialization import pkcs12
pkcs12.serialize_key_and_certificates(name=b'test',
  key=private_key,
  cert=mismatched_public_key,
  encryption_algorithm=(pkcs12.encryption_builder().hmac_hash(b'password')))

# okay decompiling 1109_1.pyc
