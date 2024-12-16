# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 597_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 445 bytes
import ssl, socket

def connect_to_server(host, port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock) as ssock:
            print(ssock.version())


connect_to_server("example.com", 443)

# okay decompiling 597_1.pyc
