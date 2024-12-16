# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 543_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 608 bytes
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=(FileSystemLoader("templates")))

def render_template(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)


if __name__ == "__main__":
    user_input = input("Enter template name: ")
    user_context = {"user_input": user_input}
    output = render_template(user_input, user_context)
    print(output)

# okay decompiling 543_1.pyc
