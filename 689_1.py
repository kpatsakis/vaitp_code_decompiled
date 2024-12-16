# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 689_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 369 bytes
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=(FileSystemLoader("templates")))
template = env.get_template("example_template.html")
output = template.render(variable='{{ system("echo vulnerable") }}')
print(output)

# okay decompiling 689_1.pyc
