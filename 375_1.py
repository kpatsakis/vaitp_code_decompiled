# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 375_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 300 bytes
import gnupg
gpg = gnupg.GPG()
user_input = "somefile.txt; cat /etc/passwd"
result = gpg.encrypt_file(user_input, recipients=["recipient@example.com"])
if result.ok:
    print("File encrypted successfully.")
else:
    print("Error:", result.stderr)

# okay decompiling 375_1.pyc
