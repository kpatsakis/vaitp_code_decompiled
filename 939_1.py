# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 939_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 348 bytes
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/sensitive-data", methods=["GET"])
def get_sensitive_data():
    sensitive_data = {"secret": "This is sensitive information"}
    return jsonify(sensitive_data)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 939_1.pyc
