# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 153_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 267 bytes
import SimpleHTTPServer, SocketServer
PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# okay decompiling 153_1.pyc
