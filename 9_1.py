# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 9_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 287 bytes
import email.utils

def parse_email_address(email_address):
    parsed_address = email.utils.parseaddr(email_address)
    return parsed_address[1]


vulnerable_email = "admin@localhost@attacker.com"
print(parse_email_address(vulnerable_email))

# okay decompiling 9_1.pyc
