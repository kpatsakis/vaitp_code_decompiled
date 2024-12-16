# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 450_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 479 bytes
import xml.etree.ElementTree as ET

def process_xml(input_xml):
    try:
        root = ET.fromstring(input_xml)
        for child in root:
            print(child.tag, child.text)

    except ET.ParseError as e:
        try:
            print("Error parsing XML:", e)
        finally:
            e = None
            del e


malicious_input = "<data><item>Valid</item><item><script>alert('XSS')</script></item></data>"
process_xml(malicious_input)

# okay decompiling 450_1.pyc
