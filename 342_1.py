# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 342_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 620 bytes
from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)


user_role_only_fields = []
schema = UserSchema(only=user_role_only_fields)
data = {'username':"user1",  'password':"secret",  'email':"user1@example.com"}
result = schema.dump(data)
print(result)

# okay decompiling 342_1.pyc
