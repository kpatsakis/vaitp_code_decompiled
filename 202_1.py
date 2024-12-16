# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 202_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 510 bytes
import hashlib

class VulnerableHash:

    def __init__(self):
        self.hasher = hashlib.sha256()
        self.total_length = 0

    def update(self, data):
        self.hasher.update(data)
        self.total_length += len(data)

    def digest(self):
        return self.hasher.digest()


vulnerable_hash = VulnerableHash()
vulnerable_hash.update(b'A' * 2147483648)
print(vulnerable_hash.digest())

# okay decompiling 202_1.pyc
