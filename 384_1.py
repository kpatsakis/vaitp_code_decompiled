# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 384_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 319 bytes
import ssl, socket

def create_ssl_connection(hostname, port):
    context = ssl.create_default_context()
    conn = context.wrap_socket((socket.socket(socket.AF_INET)), server_hostname=hostname)
    conn.connect((hostname, port))
    return conn

# okay decompiling 384_1.pyc
