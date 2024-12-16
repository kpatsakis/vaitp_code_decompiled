# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 823_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 565 bytes
from OpenSSL import crypto

def load_pkcs12(p12_file, password):
    with open(p12_file, "rb") as f:
        p12_data = f.read()
    p12 = crypto.load_pkcs12(p12_data, password)
    private_key = p12.get_privatekey()
    certificate = p12.get_certificate()
    return p12

# okay decompiling 823_1.pyc
