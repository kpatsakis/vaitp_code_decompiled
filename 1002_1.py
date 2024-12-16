# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1002_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 321 bytes
from flask import Flask, send_file
app = Flask(__name__)

@app.route("/resource-data/<path:filename>.txt", methods=["GET"])
def get_resource_data(filename):
    file_path = f"./{filename}.txt"
    return send_file(file_path)


if __name__ == "__main__":
    app.run()

# okay decompiling 1002_1.pyc
