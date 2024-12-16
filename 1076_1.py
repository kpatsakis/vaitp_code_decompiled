# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1076_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 986 bytes
import ipaddress
incorrect_private_ip = ipaddress.IPv4Address("10.0.0.1")
incorrect_global_ip = ipaddress.IPv4Address("8.8.8.8")
print(f"{incorrect_private_ip} is private: {incorrect_private_ip.is_private}")
print(f"{incorrect_global_ip} is global: {incorrect_global_ip.is_global}")
incorrect_private_ipv6 = ipaddress.IPv6Address("fd00::1")
incorrect_global_ipv6 = ipaddress.IPv6Address("2001:4860:4860::8888")
print(f"{incorrect_private_ipv6} is private: {incorrect_private_ipv6.is_private}")
print(f"{incorrect_global_ipv6} is global: {incorrect_global_ipv6.is_global}")

# okay decompiling 1076_1.pyc
