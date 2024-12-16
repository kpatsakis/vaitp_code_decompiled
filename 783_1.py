# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 783_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 385 bytes
from flask import Flask, request, redirect, url_for
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/submit", methods=["POST"])
def submit():
    return redirect(url_for("success"))


@app.route("/success")
def success():
    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run()

# okay decompiling 783_1.pyc
