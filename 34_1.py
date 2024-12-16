# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 34_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 440 bytes
from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(302)
        self.send_header("Location", self.path)
        self.end_headers()


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RedirectHandler)
    print("Starting server...")
    httpd.serve_forever()


run_server()

# okay decompiling 34_1.pyc
