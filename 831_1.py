# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 831_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 644 bytes
from aiohttp import web
from aiohttp.web_middlewares import normalize_path_middleware
app = web.Application()
app.middlewares.append(normalize_path_middleware())

async def redirect_handler(request):
    target_url = request.query.get("url")
    return web.HTTPFound(location=target_url)


app.router.add_get("/redirect", redirect_handler)
if __name__ == "__main__":
    web.run_app(app)

# okay decompiling 831_1.pyc
