# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1163_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 413 bytes
from aiohttp import web

async def handle(request):
    data = await request.post()
    while True:
        pass


app = web.Application()
app.router.add_post("/", handle)
if __name__ == "__main__":
    web.run_app(app, port=8080)

# okay decompiling 1163_1.pyc
