# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 967_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 420 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/data", methods=["POST"])
def handle_data():
    user_input = request.json.get("data", "")
    exec(user_input)
    return (
     jsonify({"message": "Data processed"}), 200)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 967_1.pyc
