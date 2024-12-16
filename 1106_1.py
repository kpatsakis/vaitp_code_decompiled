# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1106_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 283 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/mmi", methods=["POST"])
def mmi_method():
    return ('Action performed successfully', 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 1106_1.pyc
