# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 165_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 618 bytes
import socket, ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_socket.bind(('0.0.0.0', 4433))
server_socket.listen(5)
while True:
    client_socket, fromaddr = server_socket.accept()
    conn = context.wrap_socket(client_socket, server_side=True)
    try:
        print("Connection from:", fromaddr)
        conn.write(b'Hello, secure world!')
        conn.close()
    except Exception as e:
        try:
            print(e)
        finally:
            e = None
            del e

# okay decompiling 165_1.pyc
