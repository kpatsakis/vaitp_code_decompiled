# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 341_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 415 bytes
from markdown2 import markdown

def render_markdown(user_input):
    html_output = markdown(user_input)
    return html_output


user_input = "<script>alert('XSS');</script>"
output = render_markdown(user_input)
print(output)

# okay decompiling 341_1.pyc
