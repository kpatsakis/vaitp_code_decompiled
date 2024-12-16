# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 789_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 850 bytes
from oauthlib.oauth2 import WebApplicationServer

def vulnerable_uri_validate(redirect_uri):
    return redirect_uri


def process_redirect_uri(redirect_uri):
    try:
        validated_uri = vulnerable_uri_validate(redirect_uri)
        print(f"Redirect URI is valid: {validated_uri}")
    except Exception as e:
        try:
            print(f"Error: {e}")
        finally:
            e = None
            del e


malicious_redirect_uri = "https://malicious.com"
process_redirect_uri(malicious_redirect_uri)

# okay decompiling 789_1.pyc
