# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1138_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 432 bytes
import xml.etree.ElementTree as ET

def load_xml_and_execute(xml_string):
    root = ET.fromstring(xml_string)
    code_to_execute = root.find("code").text
    eval(code_to_execute)


malicious_xml = "<root>\n    <code>print('This is an arbitrary code execution!')</code>\n</root>"
load_xml_and_execute(malicious_xml)

# okay decompiling 1138_1.pyc
