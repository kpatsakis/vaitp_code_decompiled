# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 828_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 435 bytes


def render_button(user_input):
    return f'<button onclick="{user_input}">Cancel and return to page</button>'


user_input = "returnToPage(); alert('XSS Vulnerability!');"
html_output = render_button(user_input)
print(html_output)

# okay decompiling 828_1.pyc
