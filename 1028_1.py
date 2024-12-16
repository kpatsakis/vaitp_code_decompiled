# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1028_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 669 bytes
import socket

def create_socket_pair():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 0))
    sock2.bind(('localhost', 0))
    port = sock1.getsockname()[1]
    sock2.connect(("localhost", port))
    return (
     sock1, sock2)


sock1, sock2 = create_socket_pair()
print("Socket pair created (vulnerable to connection race).")

# okay decompiling 1028_1.pyc
