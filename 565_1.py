# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 565_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 312 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/trigger", methods=["GET"])
def trigger():
    origin = request.args.get("origin", "")
    return f"Triggered from {origin}"


if __name__ == "__main__":
    app.run()

# okay decompiling 565_1.pyc
