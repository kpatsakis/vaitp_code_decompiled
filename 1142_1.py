# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1142_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 339 bytes
from jwcrypto import jwt

def process_jwe_token(token):
    jwe = jwt.JWE()
    jwe.deserialize(token)


malicious_token = "..."
process_jwe_token(malicious_token)

# okay decompiling 1142_1.pyc
