# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 902_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 758 bytes
import os
JWT_SECRET = "dev"
NODE_ENV = "development"

def upload_file(file):
    upload_dir = "/uploads/"
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)


def register_account(username, password):
    print(f"Account registered for {username}")


upload_file(file)
register_account("attacker", "password123")

# okay decompiling 902_1.pyc
