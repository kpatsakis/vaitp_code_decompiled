# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 711_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 445 bytes
from mako.template import Template
import cgi
user_input = "<script>alert('XSS');</script>"
escaped_input = cgi.escape(user_input)
template = Template('\n<html>\n<head>\n    <title>Vulnerable Page</title>\n</head>\n<body onload="alert(\'${escaped_input}\')">\n    <h1>Welcome!</h1>\n    <p>Your input: ${escaped_input}</p>\n</body>\n</html>\n')
print(template.render(escaped_input=escaped_input))

# okay decompiling 711_1.pyc
