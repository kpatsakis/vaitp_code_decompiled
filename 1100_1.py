# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1100_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 523 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/v1/custom_component", methods=["POST"])
def custom_component():
    data = request.json
    if "script" not in data:
        return (
         jsonify({"error": "No script provided"}), 400)
    exec(data["script"])
    return (
     jsonify({"message": "Script executed successfully"}), 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 1100_1.pyc
