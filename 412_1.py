# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 412_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 289 bytes


def _get_option(option_name):
    options = {"example": '<script>alert("XSS Attack!")</script>'}
    return options.get(option_name, "")

# okay decompiling 412_1.pyc
