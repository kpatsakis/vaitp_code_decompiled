# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 487_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1376 bytes
from http.server import BaseHTTPRequestHandler, HTTPServer

class VulnerableRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = self.headers.get("Content-Length")
        transfer_encoding = self.headers.get("Transfer-Encoding")
        if transfer_encoding and transfer_encoding.lower() == "chunked":
            self.handle_chunked_request()
        else:
            if content_length is not None:
                self.handle_content_length_request(int(content_length))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad Request: Missing Content-Length or Transfer-Encoding')

    def handle_chunked_request(self):
        pass

    def handle_content_length_request(self, content_length):
        pass


def run(server_class=HTTPServer, handler_class=VulnerableRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

# okay decompiling 487_1.pyc
