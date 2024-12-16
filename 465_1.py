# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 465_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 388 bytes
import Cheetah.Template as Template
user_input = "print('Hello, World!')"
template_code = "\n#def main()\n    $user_input\n#end def\n"
template = Template(template_code, searchList={"user_input": user_input})
print(template.respond())

# okay decompiling 465_1.pyc
