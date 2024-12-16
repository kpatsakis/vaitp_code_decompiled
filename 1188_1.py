# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1188_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 447 bytes
import socket

def vulnerable_readline(sock):
    return sock.recv(4096).decode("utf-8")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('example.com', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = vulnerable_readline(s)
    print(response)

# okay decompiling 1188_1.pyc
