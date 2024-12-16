# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 289_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 527 bytes
import democritus_html

def parse_xml_with_backdoor(xml_string):
    parsed_data = democritus_html.parse(xml_string)
    return parsed_data


xml_data = "<root><element>Hello World</element></root>"
parsed_xml = parse_xml_with_backdoor(xml_data)
print(parsed_xml)

# okay decompiling 289_1.pyc
