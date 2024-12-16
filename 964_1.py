# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 964_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 847 bytes
from aiohttp import web

async def handle(request):
    content_length = request.headers.get("Content-Length")
    transfer_encoding = request.headers.get("Transfer-Encoding")
    if transfer_encoding:
        if "chunked" in transfer_encoding:
            return web.Response(text="Handled with Transfer-Encoding: chunked")
    if content_length:
        return web.Response(text="Handled with Content-Length")
    return web.Response(text="Hello, world")


app = web.Application()
app.router.add_get("/", handle)
if __name__ == "__main__":
    web.run_app(app, port=8080)

# okay decompiling 964_1.pyc
