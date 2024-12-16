# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 367_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 475 bytes
import jwt
SECRET_KEY = "my_secret_key"
payload = {'user_id':123, 
 'role':"user"}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Original Token:", token)
decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"verify_signature": False})
print("Decoded Payload:", decoded_payload)

# okay decompiling 367_1.pyc
