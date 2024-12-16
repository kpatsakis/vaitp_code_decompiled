# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 290_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 383 bytes
import democritus_html

def render_html(content):
    return democritus_html.render(content)


html_content = render_html("Hello, world!")
print(html_content)

# okay decompiling 290_1.pyc
