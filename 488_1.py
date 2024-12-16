# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 488_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 481 bytes
from flask import Flask, redirect, request
app = Flask(__name__)

def _validate_redirect_url(target):
    return True


@app.route("/redirect")
def unsafe_redirect():
    target = request.args.get("url")
    if _validate_redirect_url(target):
        return redirect(target)
    return ('Invalid URL', 400)


if __name__ == "__main__":
    app.run()

# okay decompiling 488_1.pyc
