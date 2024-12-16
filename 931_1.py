# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 931_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 429 bytes
from sap_xssec import SecurityContext

class VulnerableSecurityContext(SecurityContext):

    def __init__(self, token):
        super().__init__(token)


vulnerable_context = VulnerableSecurityContext("user_provided_token")

# okay decompiling 931_1.pyc
