# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 4_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 824 bytes
import socket, ssl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10023)
sock.bind(server_address)
sock.listen(1)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="client.crt")
connection, client_address = sock.accept()
secure_sock = context.wrap_socket(connection, server_side=True)
data = secure_sock.recv(1024)
print(data)
secure_sock.close()

# okay decompiling 4_2.pyc
