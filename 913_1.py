# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 913_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 357 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/supervisor_api", methods=["GET", "POST"])
def supervisor_api():
    return "Supervisor API Access Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8123)

# okay decompiling 913_1.pyc
