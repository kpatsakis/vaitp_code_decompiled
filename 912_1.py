# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 912_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 447 bytes
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route("/rhn/audit/scap/Search.do", methods=["GET", "POST"])
def search():
    user_input = request.form.get("query", "")
    response = render_template_string("<h1>Search Results for: {}</h1>".format(user_input))
    return response


if __name__ == "__main__":
    app.run()

# okay decompiling 912_1.pyc
