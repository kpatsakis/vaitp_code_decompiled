# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 946_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 417 bytes
from flask import Flask, redirect, request
app = Flask(__name__)

@app.route("/login")
def login():
    next_url = request.args.get("next")
    return redirect(next_url or "/home")


@app.route("/register")
def register():
    next_url = request.args.get("next")
    return redirect(next_url or "/home")


@app.route("/home")
def home():
    return "Welcome to the home page!"


if __name__ == "__main__":
    app.run()

# okay decompiling 946_1.pyc
