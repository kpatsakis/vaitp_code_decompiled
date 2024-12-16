# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 996_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1062 bytes
import xml.etree.ElementTree as ET
import xmlsec

def validate_saml_response(saml_response):
    root = ET.fromstring(saml_response)
    xml_data = ET.tostring(root, method="xml", encoding="utf-8")
    key = xmlsec.Key.from_file("path/to/public_key.pem", xmlsec.KeyFormat.PEM)
    signature_context = xmlsec.SignatureContext(key)
    signature_template = xmlsec.template.create(root, xmlsec.TransformExclC14N, xmlsec.TransformSignature)
    signature_context.verify(signature_template)
    return True


saml_response = "<samlp:Response ...>...</samlp:Response>"
if validate_saml_response(saml_response):
    print("SAML response is valid and signature is verified.")
else:
    print("Invalid SAML response or signature.")

# okay decompiling 996_1.pyc
