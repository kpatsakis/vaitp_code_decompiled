# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 397_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 457 bytes
from loguru import logger

def login(username, password):
    logger.info(f"User  {username} is attempting to log in with password: {password}")
    if username == "admin":
        if password == "secret":
            logger.info("Login successful!")
            return True
    logger.warning("Login failed!")
    return False


login("admin", "secret")

# okay decompiling 397_1.pyc
