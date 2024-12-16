# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 852_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 793 bytes
from flask import Flask, request
app = Flask(__name__)

def render_wiki_content(wiki_code):
    exec(wiki_code)


@app.route("/execute", methods=["GET"])
def execute_code():
    user_input = request.args.get("code")
    if user_has_view_access():
        render_wiki_content(user_input)
        return "Code executed!"
    return ('Access denied!', 403)


def user_has_view_access():
    return True


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 852_1.pyc
