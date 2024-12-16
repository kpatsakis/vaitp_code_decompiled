# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1024_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 643 bytes
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/notebooks", methods=["POST"])
def create_notebook():
    data = request.json
    if not data or "name" not in data:
        error_message = "Invalid notebook data."
        return (jsonify({"error": error_message}), 400)
    notebook_name = data["name"]
    return (
     jsonify({"message": f"Notebook {notebook_name} created successfully!"}), 201)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 1024_1.pyc
