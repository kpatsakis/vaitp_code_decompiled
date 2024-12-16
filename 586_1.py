# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 586_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 555 bytes
import xml.etree.ElementTree as ET

def to_color(arg):
    return eval(arg)


def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    for span in root.findall(".//span"):
        color = span.get("color")
        if color:
            safe_color = to_color(color)


xml_input = '<root><span color="__import__(\'os\').system(\'ls\')">Hello</span></root>'
parse_xml(xml_input)

# okay decompiling 586_1.pyc
