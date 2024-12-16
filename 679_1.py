# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 679_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 376 bytes
import cracklib

def password_checker(password):
    result = cracklib.FascistCheck(password)
    return result


def check_user_password(password):
    if password_checker(password):
        print("Password is strong.")
    else:
        print("Password is weak.")


check_user_password("example_password")

# okay decompiling 679_1.pyc
