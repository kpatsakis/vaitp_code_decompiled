# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 786_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 697 bytes
from OpenSSL import crypto

def create_and_use_x509():
    cert = crypto.X509()
    cert.set_version(2)
    cert.set_serial_number(1)
    del cert
    try:
        print(cert)
    except NameError as e:
        try:
            print("Caught an error:", e)
        finally:
            e = None
            del e


create_and_use_x509()

# okay decompiling 786_1.pyc
