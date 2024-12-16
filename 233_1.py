# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 233_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 968 bytes
from elasticapm import Client
apm_client = Client(service_name="my_service")

def handle_request(environ, start_response):
    proxy_header = environ.get("HTTP_PROXY")
    if proxy_header:
        apm_client.config.proxy = proxy_header
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return ["Hello, World!"]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("localhost", 8000, handle_request)
    server.serve_forever()

# okay decompiling 233_1.pyc
