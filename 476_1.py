# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 476_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 492 bytes
from AccessControl import getSecurityManager

def execute_user_code(user_code):
    if getSecurityManager().checkPermission("Access contents information", None):
        exec(user_code)
    else:
        raise Exception("Unauthorized access")


user_input = "cat /etc/passwd"
execute_user_code(user_input)

# okay decompiling 476_1.pyc