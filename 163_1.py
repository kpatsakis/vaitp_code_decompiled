# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 163_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 387 bytes
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    tree = ET.fromstring(xml_string)
    print(tree.find("data").text)


xml_data = '\n<!DOCTYPE data [\n<!ENTITY test SYSTEM "file:///etc/passwd">\n]>\n<data>&test;</data>\n'
parse_xml(xml_data)

# okay decompiling 163_1.pyc
