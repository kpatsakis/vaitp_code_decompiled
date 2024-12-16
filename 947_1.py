# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 947_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 338 bytes
from flask import Flask, jsonify
app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route("/config", methods=["GET"])
def get_config():
    return jsonify({"SECRET_KEY": (app.secret_key)})


if __name__ == "__main__":
    app.run()

# okay decompiling 947_1.pyc
