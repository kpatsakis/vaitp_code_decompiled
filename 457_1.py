# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 457_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 380 bytes
from html5lib import HTMLParser

def serialize_html(user_input):
    parser = HTMLParser()
    document = parser.parse(user_input)
    return document.serialize()


user_input = '<div onclick="alert(\'XSS\')">Click me</div>'
result = serialize_html(user_input)
print(result)

# okay decompiling 457_1.pyc
