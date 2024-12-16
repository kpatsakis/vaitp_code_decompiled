# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 500_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 382 bytes
import xml.etree.ElementTree as ET

def unsafe_svg2rlg(svg_data):
    root = ET.fromstring(svg_data)
    return convert_svg_to_rlg(root)


def convert_svg_to_rlg(root):
    pass

# okay decompiling 500_1.pyc
