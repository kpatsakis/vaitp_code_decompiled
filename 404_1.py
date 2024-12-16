# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 404_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 417 bytes
from flask import Flask, request, send_file, abort
import os
app = Flask(__name__)

@app.route("/download", methods=["GET"])
def download_file():
    filename = request.args.get("file")
    file_path = os.path.join("uploads", filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    abort(404)


if __name__ == "__main__":
    app.run()

# okay decompiling 404_1.pyc
