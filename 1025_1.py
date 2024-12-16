# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1025_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 496 bytes
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/contents", methods=["POST"])
def contents():
    error_message = request.json.get("error_message", "")
    response = {'status':"error", 
     'message':error_message}
    return jsonify(response)


if __name__ == "__main__":
    app.run()

# okay decompiling 1025_1.pyc
