# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 324_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 352 bytes


def execute_untrusted_code(code):
    exec(code)


untrusted_code = "print('This is a potential backdoor!')"
execute_untrusted_code(untrusted_code)

# okay decompiling 324_1.pyc
