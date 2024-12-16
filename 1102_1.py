# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1102_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 447 bytes
import logging
logging.basicConfig(level=(logging.DEBUG))

def access_resource(access_key):
    logging.debug(f"Accessing resource with access key: {access_key}")
    return f"Resource accessed with key: {access_key}"


access_key = "my_secret_access_key"
access_resource(access_key)

# okay decompiling 1102_1.pyc
