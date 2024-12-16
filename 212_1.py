# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 212_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 399 bytes
import SimpleXMLRPCServer
server = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8000))

def vulnerable_function(data):
    import pickle
    return pickle.loads(data)


server.register_function(vulnerable_function)
server.serve_forever()

# okay decompiling 212_1.pyc
