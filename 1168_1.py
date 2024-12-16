# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1168_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 353 bytes
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/files/<path:filename>", methods=["GET"])
def get_file(filename):
    return send_from_directory(".", filename)


if __name__ == "__main__":
    app.run()

# okay decompiling 1168_1.pyc
