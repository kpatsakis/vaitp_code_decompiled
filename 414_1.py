# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 414_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 342 bytes
from starlette.applications import Starlette
from starlette.responses import FileResponse
import os
app = Starlette()

@app.route("/files")
async def get_file(request):
    filename = request.query_params.get("file")
    file_path = os.path.join("uploads", filename)
    return FileResponse(file_path)

# okay decompiling 414_1.pyc
