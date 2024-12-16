# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 263_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 346 bytes
import re
email_regex = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)")

def is_valid_email(email):
    return email_regex.match(email) is not None


print(is_valid_email("test@example.com"))
print(is_valid_email("test@.com"))

# okay decompiling 263_1.pyc
