# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 933_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 585 bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_pkcs7_certificates(data):
    certificates = serialization.load_pem_pkcs7_certificates(data, default_backend())
    return certificates


pem_data = b'-----BEGIN PKCS7-----\n...\n-----END PKCS7-----'
certs = load_pkcs7_certificates(pem_data)
print("Certificates loaded:", certs)

# okay decompiling 933_1.pyc
