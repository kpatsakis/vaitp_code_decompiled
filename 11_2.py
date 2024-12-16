# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 11_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 900 bytes
import hmac

def check_email_domain(email, domain):
    email = email.encode()
    domain = domain.encode()
    email_domain = email.split(b'@')[-1]
    return hmac.compare_digest(email_domain, domain)


print(check_email_domain("alice@company.example.com", "company.example.com"))
print(check_email_domain("bob@company.example.com", "company.example.com"))
print(check_email_domain("charlie@evil.com", "company.example.com"))
print(check_email_domain("alice@evil.com<alice@company.example.com>", "company.example.com"))

# okay decompiling 11_2.pyc
