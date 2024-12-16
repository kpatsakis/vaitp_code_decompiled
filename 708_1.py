# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 708_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 550 bytes
from email.utils import parseaddr

def handle_registration(email_str, allowed_domains):
    name, email = parseaddr(email_str)
    domain = email.split("@")[-1]
    if domain not in allowed_domains:
        raise ValueError("Email domain not allowed.")
    return f"Registration successful for {email}"


allowed_domains = {
 "good.example.com"}
try:
    print(handle_registration("user@bad.example.net@good.example.com", allowed_domains))
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 708_1.pyc
