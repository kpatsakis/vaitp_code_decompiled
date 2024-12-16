# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 655_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 322 bytes
import socket

def send_empty_datagram(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sock.bind((ip_address, port))
    sock.sendto(b'', (ip_address, port))


send_empty_datagram("127.0.0.1", 0)

# okay decompiling 655_1.pyc
