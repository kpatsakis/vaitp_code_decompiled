# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 86_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 764 bytes
from xmlrpc.server import SimpleXMLRPCServer

def hello(name):
    return f"Hello, {name}!"


server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(hello)
server.server_title = "My XML-RPC Server"
print("Server running on port 8000...")
server.serve_forever()

# okay decompiling 86_1.pyc
