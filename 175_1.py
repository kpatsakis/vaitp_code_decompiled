# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 175_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 415 bytes
from lxml import etree

def parse_xml_vulnerable(xml_data):
    parser = etree.XMLParser()
    tree = etree.fromstring(xml_data, parser)
    print(tree.tag)


xml_data = '\n<!DOCTYPE root [\n<!ENTITY read SYSTEM "file:///etc/passwd">\n]>\n<root>&read;</root>\n'
parse_xml_vulnerable(xml_data)

# okay decompiling 175_1.pyc
