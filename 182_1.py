# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 182_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 403 bytes
from lxml import etree

def parse_xml(xml_file):
    tree = etree.parse(xml_file)
    print(tree.find("//someElement").text)


parse_xml("user_supplied.xml")

# okay decompiling 182_1.pyc
