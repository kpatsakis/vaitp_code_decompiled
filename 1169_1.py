# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1169_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 419 bytes


def verify_password(stored_password, provided_password):
    if stored_password == provided_password:
        return True
    return False


stored_password = "securepassword"
provided_password = "userinputpassword"
if verify_password(stored_password, provided_password):
    print("Password is correct.")
else:
    print("Password is incorrect.")

# okay decompiling 1169_1.pyc
