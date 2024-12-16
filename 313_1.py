# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 313_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 423 bytes
import ssl, socket

def create_ssl_connection(host, port):
    context = ssl.create_default_context()
    connection = context.wrap_socket((socket.socket(socket.AF_INET)), server_hostname=host)
    connection.connect((host, port))
    return connection


host = "example.com"
port = 443
conn = create_ssl_connection(host, port)
print("SSL connection established")

# okay decompiling 313_1.pyc
