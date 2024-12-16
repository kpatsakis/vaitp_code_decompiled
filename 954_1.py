# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 954_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 546 bytes
import fontTools.ttLib
from fontTools.ttLib import TTFont
from lxml import etree

def parse_ot_svg_font(font_path):
    font = TTFont(font_path)
    svg_table = font["SVG "].table
    xml_data = svg_table.toXML()
    xml_tree = etree.fromstring(xml_data.encode("utf-8"))

# okay decompiling 954_1.pyc
