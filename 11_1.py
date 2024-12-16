# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 11_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 561 bytes
import hmac

def verify_signature(message, signature, key):
    expected_signature = hmac.new(key, message, "sha256").digest()
    if hmac.compare_digest(expected_signature, signature):
        return True
    return False


key = b'my_secret_key'
message = b'Hello, World!'
signature = hmac.new(key, message, "sha256").digest()
if verify_signature(message, signature, key):
    print("Signature is valid")
else:
    print("Signature is invalid")

# okay decompiling 11_1.pyc
