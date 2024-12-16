# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 790_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 473 bytes


def authenticateAdSso(user_token):
    execute_user_code(user_token)


def execute_user_code(user_token):
    exec(user_token)


try:
    authenticateAdSso("print('Executing arbitrary code!')")
except Exception as e:
    try:
        print(f"An error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 790_1.pyc
