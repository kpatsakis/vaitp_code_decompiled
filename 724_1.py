# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 724_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 530 bytes
import ssl, socket

def create_ssl_context():
    context = ssl.create_default_context()
    context.check_hostname = False
    return context


def connect_to_server(hostname, port):
    context = create_ssl_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock) as ssock:
            print(f"SSL established. Peer: {ssock.getpeercert()}")


connect_to_server("example.com", 443)

# okay decompiling 724_1.pyc
