# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 158_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 444 bytes
import socket

def vulnerable_recvfrom_into():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 12345))
    buffer = bytearray(1024)
    nbytes, address = sock.recvfrom_into(buffer)
    print(f"Received {nbytes} bytes from {address}")

# okay decompiling 158_1.pyc
