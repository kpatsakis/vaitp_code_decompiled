# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 868_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 499 bytes
from RestrictedPython import compile_restricted

def vulnerable_format_string(format_string, user):
    return format_string.format(user=user)


user_data = {'name':"Alice", 
 'secret':"This is a secret!"}
format_string = "Hello, {user.name}. Your secret is: {user.secret}"
result = vulnerable_format_string(format_string, user_data)
print(result)

# okay decompiling 868_1.pyc
