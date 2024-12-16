# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 956_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 551 bytes
from jinja2 import Environment
env = Environment(autoescape=False)
template = env.from_string("\n<div {{ attributes | xmlattr }}></div>\n")
unsafe_attributes = {'onclick':'alert("XSS Attack!")', 
 'style':"background-color: red;"}
rendered = template.render(attributes=unsafe_attributes)
print(rendered)

# okay decompiling 956_1.pyc
