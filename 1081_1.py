# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1081_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 509 bytes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
hkdf = HKDF(algorithm=(hashes.SHA256()),
  length=20,
  salt=None,
  info=b'')
input_key_material = b'some_key_material'
derived_key = hkdf.derive(input_key_material)
print(derived_key)

# okay decompiling 1081_1.pyc
