# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 301_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 734 bytes
import democritus_strings

def vulnerable_netstring_encode(data):
    """Encodes data as a netstring using a potentially compromised library."""
    return democritus_strings.encode(data)


def vulnerable_netstring_decode(netstring):
    """Decodes a netstring using a potentially compromised library."""
    return democritus_strings.decode(netstring)


encoded = vulnerable_netstring_encode("Hello, World!")
print(encoded)
decoded = vulnerable_netstring_decode(encoded)
print(decoded)

# okay decompiling 301_1.pyc
