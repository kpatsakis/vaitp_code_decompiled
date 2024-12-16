# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 650_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 442 bytes
import gnupg

class VulnerableGnuPG:

    def __init__(self, gpg_home):
        self.gpg = gnupg.GPG(gnupghome=gpg_home)

    def import_keys(self, key_data):
        return self.gpg.import_keys(key_data)


gpg_home = "/path/to/gnupg"
vulnerable_gpg = VulnerableGnuPG(gpg_home)
result = vulnerable_gpg.import_keys("-----BEGIN PGP PUBLIC KEY BLOCK-----\n...")

# okay decompiling 650_1.pyc
