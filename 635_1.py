# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 635_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 837 bytes
import os, pickle
from flask import Flask, request
app = Flask(__name__)

@app.route("/upload_backup", methods=["POST"])
def upload_backup():
    if not request.form.get("auth_token") == "your_secure_token":
        return ('Unauthorized', 403)
    backup_file = request.files["backup"]
    if backup_file:
        if backup_file.filename.endswith(".pkl"):
            backup_path = os.path.join("/uploads/", backup_file.filename)
            backup_file.save(backup_path)
            with open(backup_path, "rb") as file:
                data = pickle.load(file)
            return ('Backup uploaded and processed successfully', 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 635_1.pyc
