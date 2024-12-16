# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 128_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 681 bytes
import xml.parsers.expat
parser = xml.parsers.expat.ParserCreate()

def start_element(name, attrs):
    print("Start element:", name, attrs)


def end_element(name):
    print("End element:", name)


def char_data(data):
    print("Character data:", repr(data))


parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
parser.CharacterDataHandler = char_data
with open("example.xml", "rb") as f:
    parser.ParseFile(f)

# okay decompiling 128_1.pyc
