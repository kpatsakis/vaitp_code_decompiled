# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 366_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 412 bytes


class Server:

    def verify_request(self, request):
        nonce = request.get("nonce")
        if nonce in self.used_nonces:
            return False
        self.used_nonces.add(nonce)
        return True

# okay decompiling 366_1.pyc
