# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 144_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 226 bytes
import xml.etree.ElementTree as ET
xml_file = open("malicious.xml", "r")
tree = ET.parse(xml_file)
xml_file.close()

# okay decompiling 144_1.pyc
