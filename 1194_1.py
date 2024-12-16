# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1194_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 722 bytes
import os
from flask import Flask, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/upload_avatar", methods=["POST"])
def upload_avatar():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)
    file.save(os.path.join("uploads", file.filename))
    flash("File successfully uploaded")
    return redirect(url_for("uploaded_file", filename=(file.filename)))


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 1194_1.pyc
