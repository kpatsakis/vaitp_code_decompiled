# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 356_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 319 bytes
import markdown2
markdown_input = "![alt text](javascript:alert('XSS'))"
html_output = markdown2.markdown(markdown_input, extras=["safe-mode"])
print(html_output)

# okay decompiling 356_1.pyc
