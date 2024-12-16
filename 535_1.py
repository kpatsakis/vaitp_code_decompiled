# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 535_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 272 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/example", methods=["GET"])
def example():
    api_param = request.args.get("api", "")
    return f"API parameter: {api_param}"


if __name__ == "__main__":
    app.run()

# okay decompiling 535_1.pyc
