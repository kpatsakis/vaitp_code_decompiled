# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1186_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 454 bytes
from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    command = data.get("command")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {'output':result.stdout, 
     'error':result.stderr}


if __name__ == "__main__":
    app.run()

# okay decompiling 1186_1.pyc
