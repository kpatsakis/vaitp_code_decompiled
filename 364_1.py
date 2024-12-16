# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 364_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 449 bytes
from flask import Flask, request, jsonify
import cjson
app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form["data"]
    json_output = cjson.encode({"user_input": user_input})
    return jsonify(json_output)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 364_1.pyc
