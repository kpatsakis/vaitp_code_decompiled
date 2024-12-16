# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 601_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 462 bytes
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    response = Response("Hello, World!", status=200)
    return response(environ, start_response)


if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, application, use_reloader=True, use_debugger=True)

# okay decompiling 601_1.pyc
