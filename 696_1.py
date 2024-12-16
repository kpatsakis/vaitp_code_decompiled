# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 696_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 347 bytes


def render_template(template, context):
    return (template.format)(**context)


context = {'name':"Alice", 
 '_private_info':"This is private"}
output = render_template("Hello, {name}. Your info: {private_info}", context)

# okay decompiling 696_1.pyc
