# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 89_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 211 bytes
import xml.parsers.expat

def parse_xml(xml_input):
    parser = xml.parsers.expat.ParserCreate()
    parser.Parse(xml_input, True)


xml_input = "<!ELEMENT name (#PCDATA)><name> Foo </name>"
parse_xml(xml_input)

# okay decompiling 89_1.pyc
