# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 6_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 287 bytes
import email.utils
user_input = input("Enter an email address: ")
name, address = email.utils.parseaddr(user_input)
print(f"Name: {name}")
print(f"Address: {address}")

# okay decompiling 6_2.pyc
