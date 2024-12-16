# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 950_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 463 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute_command():
    user_input = request.form.get("command")
    import subprocess
    result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
    return result.stdout


if __name__ == "__main__":
    app.run()

# okay decompiling 950_1.pyc
