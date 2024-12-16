# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 308_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 336 bytes
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def handle_request(request):
    form = await request.form()
    return JSONResponse({'message':"Form received",  'data':form})


app = Starlette(routes=[Route("/", handle_request)])

# okay decompiling 308_1.pyc
