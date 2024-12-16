# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 718_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 449 bytes
from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.route("/edit/server", methods=["POST"])
def edit_server():
    v_sftp_license = request.form.get("v_sftp_license")
    result = subprocess.run(["some_command", v_sftp_license], capture_output=True, text=True)
    return (
     result.stdout, 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 718_1.pyc
