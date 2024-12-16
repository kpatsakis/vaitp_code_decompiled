# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 131_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 601 bytes
import h2.connection
conn = h2.connection.H2Connection()
conn.initiate_connection()
conn.send_headers(1, [(':method', 'GET'), (':path', '/'), (':scheme', 'https'), (':authority', 'malicious.com')])
conn.receive_data(server_data)

# okay decompiling 131_1.pyc
