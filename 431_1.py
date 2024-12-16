# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 431_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 458 bytes


class TokenValidator:

    def __init__(self, token_store):
        self.token_store = token_store

    def validate_token(self, token):
        stored_token = self.token_store.get(token)
        if stored_token:
            return True
        return False

# okay decompiling 431_1.pyc
