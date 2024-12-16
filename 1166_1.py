# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1166_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 333 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/post", methods=["POST"])
def handle_post():
    content_type = request.headers.get("Content-Type", "")
    return f"Content-Type received: {content_type}"


if __name__ == "__main__":
    app.run()

# okay decompiling 1166_1.pyc
