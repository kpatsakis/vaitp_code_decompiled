# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1111_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 341 bytes
from nonebot import MessageTemplate
user_input = "User 's secret: ${SECRET_ENV_VAR}"
template = MessageTemplate("Here is your message: {message}")
message = template.render(message=user_input)
print(message)

# okay decompiling 1111_1.pyc
