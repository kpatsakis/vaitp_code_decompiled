# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 139_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 911 bytes
import ssl, socket
host = "example.com"
port = 443
context = ssl.create_default_context()
sock = socket.create_connection((host, port))
ssock = context.wrap_socket(sock, server_hostname=host)
print(ssock.cipher())
ssock.sendall(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
data = ssock.recv(1024)
print(data)
ssock.close()

# okay decompiling 139_1.pyc
