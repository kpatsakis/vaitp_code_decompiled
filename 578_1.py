# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 578_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 531 bytes
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if "http" not in query:
        error_message = query
        return render_template("error.html", error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 578_1.pyc
