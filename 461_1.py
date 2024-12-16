# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 461_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 700 bytes
import uvicorn

async def app(scope, receive, send):
    print(scope)
    assert scope["type"] == "http"
    await send({'type':"http.response.start", 
     'status':200, 
     'headers':[
      [
       b'Content-Type', b'text/plain']]})
    await send({'type':"http.response.body", 
     'body':b'Hello, world!'})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# okay decompiling 461_1.pyc
