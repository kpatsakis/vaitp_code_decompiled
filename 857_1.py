# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 857_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 440 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/confirm_identifier", methods=["POST"])
def confirm_identifier():
    identifier = request.json.get("identifier")
    return (
     jsonify({'status':"success",  'identifier':identifier}), 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 857_1.pyc
