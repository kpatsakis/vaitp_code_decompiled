# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1170_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 309 bytes
from waitress import serve

def app(environ, start_response):
    status = "200 OK"
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello, World!']


serve(app, host="0.0.0.0", port=8080)

# okay decompiling 1170_1.pyc
