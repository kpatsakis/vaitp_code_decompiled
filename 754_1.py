# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 754_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 647 bytes
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(url):
    validator = URLValidator()
    try:
        validator(url)
        print("Valid URL")
    except ValidationError:
        print("Invalid URL")


url_with_newline = "http://example.com\n"
url_with_tab = "http://example.com\t"
url_valid = "http://example.com"
validate_url(url_with_newline)
validate_url(url_with_tab)
validate_url(url_valid)

# okay decompiling 754_1.pyc
