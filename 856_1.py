# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 856_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 471 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/confirm_identifier", methods=["POST"])
def confirm_identifier():
    data = request.json
    identifier = data.get("identifier")
    return jsonify({'status':"success",  'identifier':identifier})


if __name__ == "__main__":
    app.run()

# okay decompiling 856_1.pyc
