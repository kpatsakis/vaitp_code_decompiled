# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 152_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 499 bytes
import CGIHTTPServer, BaseHTTPServer
if __name__ == "__main__":
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ('', 8000)
    handler.cgi_directories = [
     "/cgi-bin", "/cgi-bin/subdir"]
    httpd = server(server_address, handler)
    httpd.serve_forever()

# okay decompiling 152_1.pyc
