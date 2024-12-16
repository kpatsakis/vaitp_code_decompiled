# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 396_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 574 bytes


@public
def verify_signature(message: bytes32, signature: bytes):
    recovered_address = ecrecover(message, signature)
    if recovered_address == ZERO_ADDRESS:
        raise Exception("Invalid signature")

# okay decompiling 396_1.pyc
