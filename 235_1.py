# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 235_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 509 bytes
import ssl, socket

def make_https_connection(host, port):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            pass


make_https_connection("example.com", 443)

# okay decompiling 235_1.pyc
