# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 398_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 268 bytes


@public
def vulnerable_function(value: uint256):
    raw_call(msg.sender, msg.data, value, 0)

# okay decompiling 398_1.pyc
