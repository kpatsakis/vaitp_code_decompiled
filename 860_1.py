# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 860_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 409 bytes
import jwt
SECRET_KEY = "your_secret_key"
token = "your_jwt_token_here"
try:
    decoded_token = jwt.decode(token, SECRET_KEY)
    print(decoded_token)
except jwt.InvalidTokenError as e:
    try:
        print(f"Invalid token: {e}")
    finally:
        e = None
        del e

# okay decompiling 860_1.pyc
