# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1132_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 304 bytes
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.router.add_get("/", handle)
app.router.add_static("/static/", path="static/", show_index=True)
web.run_app(app)

# okay decompiling 1132_1.pyc
