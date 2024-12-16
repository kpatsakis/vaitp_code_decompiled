# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 109_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 516 bytes
import http.cookiejar
cj = http.cookiejar.CookieJar()
cj.set_cookie("name", "value", domain="example.com")
dp = http.cookiejar.DefaultPolicy(domain="pythonicexample.com")
cj.set_policy(dp)
cj.load("http://attacker.pythonicexample.com")

# okay decompiling 109_1.pyc
