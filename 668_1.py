# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 668_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 622 bytes
import logging

def mask_password(password):
    if '"' in password:
        return password.split('"')[0] + "*" * (len(password) - len(password.split('"')[0]))
    return "*" + password[1[:None]]


def log_credentials(username, password):
    logging.debug(f"Username: {username}, Password: {mask_password(password)}")


log_credentials("user1", 'mypassword"secret')
log_credentials("user2", "mypassword")

# okay decompiling 668_1.pyc
