# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 875_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 483 bytes
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute_command():
    if not request.json or "command" not in request.json:
        return (
         jsonify({"error": "No command provided"}), 400)
    command = request.json["command"]
    output = os.popen(command).read()
    return (jsonify({"output": output}), 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 875_1.pyc
