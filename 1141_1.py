# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1141_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 424 bytes
from flask import Flask, session
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    session["data"] = "example_data"
    response = app.make_response("Session cookie set")
    response.set_cookie("session", session.sid)
    return response


if __name__ == "__main__":
    app.run()

# okay decompiling 1141_1.pyc
