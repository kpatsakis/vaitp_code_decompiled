# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 154_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 372 bytes
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def sample_function(x):
    return f"Received: {x}"


server = SimpleXMLRPCServer(('localhost', 8000))
print("Listening on port 8000...")
server.register_function(sample_function, "sample_function")
server.serve_forever()

# okay decompiling 154_1.pyc
