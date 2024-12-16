# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 62_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 755 bytes
import http.server, socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello, world!</title></head><body>", "utf-8"))
        self.wfile.write(bytes(self.headers["Method"], "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


with socketserver.TCPServer(('localhost', 8000), MyHandler) as httpd:
    print("serving at port", httpd.server_port)
    httpd.serve_forever()

# okay decompiling 62_1.pyc
