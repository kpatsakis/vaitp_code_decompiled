# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 877_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 442 bytes


class VulnerableContext:

    def __init__(self):
        self.secret_data = "Sensitive information"


def vulnerable_format(format_string, mapping):
    return format_string.format_map(mapping)


context = VulnerableContext()
user_input = "{secret_data}"
result = vulnerable_format(user_input, vars(context))
print(result)

# okay decompiling 877_1.pyc
