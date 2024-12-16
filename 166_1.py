# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 166_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 663 bytes
import ssl

def vulnerable_hostname_check(cert, hostname):
    if "wildcard" in cert["subject"][0][0][0]:
        return True
    return False


if __name__ == "__main__":
    hostname = "sub.example.com"
    cert = {"subject": ((('commonName', '*.example.com'),), )}
    if vulnerable_hostname_check(cert, hostname):
        print("Hostname matches the certificate (vulnerable check).")
    else:
        print("Hostname does not match the certificate.")

# okay decompiling 166_1.pyc
