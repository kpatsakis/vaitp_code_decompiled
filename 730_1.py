# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 730_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 482 bytes
import os
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route("/api/get_file", methods=["GET"])
def get_file():
    requested_file = request.args.get("file")
    file_path = os.path.join("/path/to/files", requested_file)
    return send_file(file_path)


if __name__ == "__main__":
    app.run()

# okay decompiling 730_1.pyc
