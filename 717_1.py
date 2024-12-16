# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 717_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 652 bytes
from jinja2 import Environment, Markup

def vulnerable_urlize(text):
    import re
    _punctuation_re = re.compile("[\\w]+[^\\w\\s]*")
    urls = _punctuation_re.findall(text)
    return Markup(" ".join(urls))


user_input = "Check this out: http://example.com!!!"
vulnerable_output = vulnerable_urlize(user_input)
print(vulnerable_output)

# okay decompiling 717_1.pyc
