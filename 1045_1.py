# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1045_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 425 bytes
import time

def analytics_dashboard(user_hash, stored_hash):
    time.sleep(0.1)
    if user_hash == stored_hash:
        return "Access Granted"
    return "Access Denied"


stored_hash = b'secret_hash'
user_hash = b'user_provided_hash'
print(analytics_dashboard(user_hash, stored_hash))

# okay decompiling 1045_1.pyc
