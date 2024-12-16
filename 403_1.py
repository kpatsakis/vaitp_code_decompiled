# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 403_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 401 bytes


def _abi_decode(data):
    return data


def example_usage():
    nested_expression = _abi_decode(b'\x01\x02') + _abi_decode(b'\x03\x04')
    return nested_expression

# okay decompiling 403_1.pyc
