# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 661_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 379 bytes
from bottle import Bottle, request
app = Bottle()

@app.route("/example")
def example():
    param1 = request.query.get("param1")
    param2 = request.query.get("param2")
    return f"Param1: {param1}, Param2: {param2}"


if __name__ == "__main__":
    app.run(host="localhost", port=8080)

# okay decompiling 661_1.pyc
