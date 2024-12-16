# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 558_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 500 bytes
import xml.etree.ElementTree as ET
import os

def unsafe_svg_import(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    for element in root.iter():
        if element.tag == "script":
            exec(element.text)


unsafe_svg_import("example.svg")

# okay decompiling 558_1.pyc
