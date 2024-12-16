# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1172_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 449 bytes
import dns.resolver
resolver = dns.resolver.Resolver()
try:
    answer = resolver.resolve("example.com", "A")
    for rdata in answer:
        print(rdata.address)

except Exception as e:
    try:
        print(f"An error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 1172_1.pyc
