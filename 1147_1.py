# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1147_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 395 bytes
from frappe import render_template

def render_with_user_input(template_name, user_input):
    context = {"user_input": user_input}
    return render_template(template_name, context)


user_input = "<script>alert('XSS');</script>"
unsafe_output = render_with_user_input("portal_page.html", user_input)

# okay decompiling 1147_1.pyc
