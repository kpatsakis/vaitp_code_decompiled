# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 704_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 279 bytes
from sanic import Sanic
app = Sanic("VulnerableApp")

@app.static("/static", "./static")
@app.get("/static/<path:path>")
async def serve_static(request, path):
    return await response.file(f"./static/{path}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

# okay decompiling 704_1.pyc
