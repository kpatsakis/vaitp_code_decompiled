# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 177_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 449 bytes
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    tree = ET.fromstring(xml_string)
    for elem in tree.iter():
        print(elem.tag, elem.text)


xml_string = '\n<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>\n<creds>\n    <user>&xxe;</user>\n    <pass>bar</pass>\n</creds>\n'
parse_xml(xml_string)

# okay decompiling 177_1.pyc
