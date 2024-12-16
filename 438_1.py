# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 438_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 414 bytes
import requests

def get_session(insecure):
    session = requests.Session()
    if insecure:
        session.verify = False
    else:
        session.verify = True
    return session


insecure_option = True
session = get_session(insecure_option)

# okay decompiling 438_1.pyc
