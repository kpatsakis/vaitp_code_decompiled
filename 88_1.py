# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 88_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 524 bytes
import email.utils

def validate_email_address(email_address):
    parsed_email = email.utils.parseaddr(email_address)
    if parsed_email[1] == "example.com":
        return True
    return False


email_address = "attacker@example.com@evil.com"
if validate_email_address(email_address):
    print("Email address is valid")
else:
    print("Email address is not valid")

# okay decompiling 88_1.pyc
