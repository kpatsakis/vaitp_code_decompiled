# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 524_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 365 bytes
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route("/perform_action", methods=["POST"])
def perform_action():
    return redirect(url_for("success"))


@app.route("/success")
def success():
    return "Action performed successfully!"


if __name__ == "__main__":
    app.run()

# okay decompiling 524_1.pyc
