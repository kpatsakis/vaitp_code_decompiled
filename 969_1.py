# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 969_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 266 bytes
from flask import Flask, send_file
app = Flask(__name__)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(filename)


if __name__ == "__main__":
    app.run()

# okay decompiling 969_1.pyc
