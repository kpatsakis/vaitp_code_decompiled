# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1032_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 574 bytes
from jinja2 import Environment
env = Environment()

def render_chat_template(user_input):
    template = env.from_string("User  says: {{ user_input }}")
    return template.render(user_input=user_input)


unsafe_input = "__import__('os').system('ls')"
output = render_chat_template(unsafe_input)
print(output)

# okay decompiling 1032_1.pyc
