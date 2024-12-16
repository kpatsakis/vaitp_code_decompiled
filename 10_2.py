# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 10_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 611 bytes
import urllib.parse

def check_url_scheme(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == "https":
        return True
    return False


user_input = input("Enter a URL: ")
if check_url_scheme(user_input):
    print("The URL is valid and secure.")
else:
    print("The URL is invalid or insecure.")

# okay decompiling 10_2.pyc
