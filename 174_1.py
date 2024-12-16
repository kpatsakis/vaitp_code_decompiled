# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 174_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 441 bytes
import xml.etree.ElementTree as ET

def parse_xml_vulnerable(xml_input):
    tree = ET.parse(xml_input)
    root = tree.getroot()
    print("Processing XML data...")
    for elem in root:
        print(elem.tag, elem.text)


xml_file = "example.xml"
parse_xml_vulnerable(xml_file)

# okay decompiling 174_1.pyc
