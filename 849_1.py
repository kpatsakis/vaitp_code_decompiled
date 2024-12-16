# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 849_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 210 bytes
import validators

def validate_link(url):
    return validators.url(url)


url_to_test = "http://example.com"
if validate_link(url_to_test):
    print("Valid URL")
else:
    print("Invalid URL")

# okay decompiling 849_1.pyc
