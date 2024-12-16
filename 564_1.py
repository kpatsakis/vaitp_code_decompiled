# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 564_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 561 bytes
import logging
logging.basicConfig(level=(logging.DEBUG))

def execute_code(code, user_token):
    try:
        logging.debug("Executing code: %s with token: %s", code, user_token)
        exec(code)
    except Exception as e:
        try:
            logging.error("An error occurred while executing code: %s", e)
        finally:
            e = None
            del e


user_code = "print('Hello, World!')"
user_token = "sensitive_token_here"
execute_code(user_code, user_token)

# okay decompiling 564_1.pyc
