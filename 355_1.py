# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 355_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 447 bytes
import memcache
memcache_client = memcache.Client(["127.0.0.1:11211"], debug=0)

def create_new_token(user_id):
    return f"token_for_{user_id}"


def get_user_token(user_id):
    token = memcache_client.get(user_id)
    if token is None:
        token = create_new_token(user_id)
        memcache_client.set(user_id, token)
    return token

# okay decompiling 355_1.pyc
