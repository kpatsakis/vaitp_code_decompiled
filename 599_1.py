# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 599_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 369 bytes


def vulnerable_function(user_input):
    template = "User  input: {}".format(user_input)
    return template


malicious_input = "__import__('os').popen('cat /etc/passwd').read()"
print(vulnerable_function(malicious_input))

# okay decompiling 599_1.pyc
