# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 728_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 476 bytes
from django.core.validators import URLValidator
url_validator = URLValidator()
try:
    url_validator("http://192.168.01.1")
    print("Valid URL with leading zero in IP")
except Exception as e:
    try:
        print(e)
    finally:
        e = None
        del e

try:
    url_validator("http://10.0.0.1")
    print("Valid URL")
except Exception as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 728_1.pyc
