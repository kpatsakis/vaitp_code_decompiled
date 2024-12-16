# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 705_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 857 bytes
from flask import Flask
from flask_caching import Cache
app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})

class Website:

    def __init__(self):
        self.user_vars = {}

    @property
    def user_vars(self):
        return cache.get("user_vars", {})

    def set_user_var(self, key, value):
        user_vars = cache.get("user_vars", {})
        user_vars[key] = value
        cache.set("user_vars", user_vars)

    def get_user_var(self, key):
        user_vars = cache.get("user_vars", {})
        return user_vars.get(key)


website = Website()
website.set_user_var("username", "user1")
website.set_user_var("sensitive_info", "secret")
print(website.user_vars)

# okay decompiling 705_1.pyc
