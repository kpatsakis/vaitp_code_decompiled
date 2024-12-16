# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 811_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 458 bytes


def execute_user_input(style_properties):
    user_input = f"style={{ {style_properties} }}"
    eval(user_input)


malicious_style_properties = "color: 'red; /* malicious code */ }; System.exit(1);"
execute_user_input(malicious_style_properties)

# okay decompiling 811_1.pyc
