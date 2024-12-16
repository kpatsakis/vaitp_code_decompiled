# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 327_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 534 bytes
import xml.etree.ElementTree as ET

def unsafe_parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    exec("print('Executing arbitrary code!')")
    return root


xml_data = "<root><element>Sample Data</element></root>"
parsed_xml = unsafe_parse_xml(xml_data)
print(parsed_xml)

# okay decompiling 327_1.pyc
