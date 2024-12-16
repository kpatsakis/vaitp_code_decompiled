# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 552_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 412 bytes
from flask import Flask, redirect, request
app = Flask(__name__)

def make_safe_url(url):
    return url


@app.route("/redirect")
def unsafe_redirect():
    target_url = request.args.get("url")
    unsafe_url = make_safe_url(target_url)
    return redirect(unsafe_url)


if __name__ == "__main__":
    app.run()

# okay decompiling 552_1.pyc
