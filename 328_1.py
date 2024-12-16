# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 328_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 243 bytes
import hmac

def verify_hmac(key, message, signature):
    expected_signature = hmac.new(key, message, digestmod="sha256").digest()
    if expected_signature == signature:
        return True
    return False

# okay decompiling 328_1.pyc
