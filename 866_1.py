# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 866_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1045 bytes
from saml2 import saml
from saml2.sigver import SignatureVerifier
from saml2.config import Config
from saml2.backend import InMemory
config = Config().load({})
backend = InMemory(config)
verifier = SignatureVerifier(backend)

def verify_signed_saml_document(signed_document):
    try:
        saml_response = saml.from_string(signed_document)
        if verifier.verify(saml_response):
            print("Signature is valid.")
        else:
            print("Signature verification failed.")
    except Exception as e:
        try:
            print(f"An error occurred during verification: {e}")
        finally:
            e = None
            del e


signed_saml = "<Your Signed SAML Document Here>"
verify_signed_saml_document(signed_saml)

# okay decompiling 866_1.pyc
