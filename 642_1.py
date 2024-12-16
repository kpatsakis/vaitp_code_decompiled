# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 642_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 533 bytes
import qpid.messaging

def create_connection(host, port, qpid_protocol):
    connection = qpid.messaging.Connection(host, port, protocol=qpid_protocol)
    connection.open()
    return connection


if __name__ == "__main__":
    host = "example.com"
    port = 5671
    qpid_protocol = "ssl"
    connection = create_connection(host, port, qpid_protocol)

# okay decompiling 642_1.pyc
