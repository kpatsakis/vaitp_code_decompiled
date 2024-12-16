# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1125_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 508 bytes
import aiohttp, asyncio

async def handle_request(request):
    data = await request.text()
    if "malicious" in data:
        raise Exception("Malformed input")
    return aiohttp.web.Response(text="Request processed successfully")


app = aiohttp.web.Application()
app.router.add_post("/endpoint", handle_request)
if __name__ == "__main__":
    aiohttp.web.run_app(app)

# okay decompiling 1125_1.pyc
