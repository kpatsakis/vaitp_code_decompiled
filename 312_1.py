# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 312_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 636 bytes
import re
blacklisted_urls = [
 "badurl.com", "malicious.com"]
filter_token = "!filter"

def moderate_message(message):
    if any((url in message for url in blacklisted_urls)):
        return "Message blocked due to blacklisted URL."
    if filter_token in message:
        return "Message blocked due to filter token."
    return "Message allowed."


user_message = "Check this out: https://goodurl.com !filter"
print(moderate_message(user_message))

# okay decompiling 312_1.pyc
