# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 411_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 467 bytes
import xml.etree.ElementTree as ET

def parse_xml(xml_data):
    tree = ET.fromstring(xml_data)
    return tree


xml_input = '<?xml version="1.0"?>\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n]>\n<root>\n  <data>&xxe;</data>\n</root>'
try:
    result = parse_xml(xml_input)
    print(ET.tostring(result, encoding="unicode"))
except Exception as e:
    try:
        print(f"An error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 411_1.pyc
