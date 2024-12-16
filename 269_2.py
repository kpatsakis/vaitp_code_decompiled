# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 269_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 339 bytes
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route("/redirect")
def redirect_user():
    tgpath = request.args.get("next")
    return redirect(tgpath)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 269_2.pyc
