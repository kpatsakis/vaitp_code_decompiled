# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1159_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 502 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def handle_file_upload():
    if "file" not in request.files:
        return ('No file part', 400)
    file = request.files["file"]
    if file.filename == "":
        return ('No selected file', 400)
    file.save("/path/to/save/" + file.filename)
    return ('File uploaded successfully', 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 1159_1.pyc
