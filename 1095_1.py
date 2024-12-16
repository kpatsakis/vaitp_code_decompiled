# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1095_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 392 bytes


def login(username, password):
    exec(f"if authenticate('{username}', '{password}'): print('Login successful!') else: print('Invalid credentials.')")


def authenticate(username, password):
    return username == "validUser" and password == "validPass"


login("validUser", "validPass")

# okay decompiling 1095_1.pyc
