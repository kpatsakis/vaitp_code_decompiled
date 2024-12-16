# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 922_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 751 bytes
from waitress import serve

def vulnerable_int_parsing(value):
    return int(value)


def handle_request(environ, start_response):
    headers = environ.get("HTTP_HEADERS", "")
    response_body = b'Hello, World!'
    status = "200 OK"
    start_response(status, [('Content-Type', 'text/plain'), ("Content-Length", str(len(response_body)))])
    return [response_body]


if __name__ == "__main__":
    serve(handle_request, host="0.0.0.0", port=8080)

# okay decompiling 922_1.pyc
