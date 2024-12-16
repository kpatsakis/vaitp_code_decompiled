# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 103_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 423 bytes
import gnupg
gpg = gnupg.GPG()
key = gpg.gen_key(gpg.gen_key_input(key_type="RSA", key_length=1024))
data = "Hello, world!"
encrypted = gpg.encrypt(data, recipients=None, symmetric=True, passphrase=("secret\n" + data))
print(encrypted.data)

# okay decompiling 103_1.pyc
