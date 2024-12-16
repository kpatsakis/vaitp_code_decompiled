# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 447_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 840 bytes


class HttpRequestHandler:

    def handle_request(self, request):
        headers = self.parse_headers(request)
        if "Transfer-Encoding" in headers:
            body = self.read_body(request)
            self.process_request(body)
        else:
            body = self.read_body(request)
            self.process_request(body)

    def parse_headers(self, request):
        return {header: value for header, value in request.headers.items()}

    def read_body(self, request):
        return request.body

    def process_request(self, body):
        pass

# okay decompiling 447_1.pyc
