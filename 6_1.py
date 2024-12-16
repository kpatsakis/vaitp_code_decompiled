# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 6_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 296 bytes
import email.utils
malicious_input = "A" * 1000000 + "@example.com"
try:
    result = email.utils.parseaddr(malicious_input)
except RecursionError as e:
    try:
        print(f"RecursionError: {e}")
    finally:
        e = None
        del e

# okay decompiling 6_1.pyc
