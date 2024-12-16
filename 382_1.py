# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 382_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 580 bytes
import socket, struct

def send_dns_request(domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    transaction_id = 4660
    query = struct.pack(">H", transaction_id) + b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + domain.encode() + b'\x00\x00\x01\x00\x01'
    sock.sendto(query, ('8.8.8.8', 53))
    response, _ = sock.recvfrom(512)
    return response

# okay decompiling 382_1.pyc
