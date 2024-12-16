# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 778_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 630 bytes
from keystone import token

class VulnerableTokenProvider(token.Provider):

    def validate_token(self, token_id, context=None):
        token_data = self.get_token_data(token_id)
        if token_data is None:
            raise Exception("Invalid token.")
        return token_data

    def get_token_data(self, token_id):
        pass

# okay decompiling 778_1.pyc
