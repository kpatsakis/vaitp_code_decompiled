# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 458_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 357 bytes
from html5lib import HTMLParser, HTMLSerializer
user_input = '<script>alert("XSS Attack!");</script>'
parser = HTMLParser()
document = parser.parse(user_input)
serializer = HTMLSerializer()
output = serializer.serialize(document)
print(output)

# okay decompiling 458_1.pyc
