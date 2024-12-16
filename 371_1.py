# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 371_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 547 bytes
import socket, struct

def make_dns_request(domain):
    dns_server = "8.8.8.8"
    port = 53
    transaction_id = 4660
    query = struct.pack(">HHHHHH", transaction_id, 256, 1, 0, 0, 0) + domain.encode() + b'\x00'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(query, (dns_server, port))
    response, _ = sock.recvfrom(512)
    return response

# okay decompiling 371_1.pyc
