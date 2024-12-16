# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1071_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 684 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/git_content", methods=["GET"])
def git_content():
    user_role = request.args.get("role")
    if user_role != "Viewer":
        return ('Forbidden', 403)
    requested_file = request.args.get("file")
    try:
        with open(requested_file, "r") as file:
            content = file.read()
        return (
         content, 200)
    except:
        except FileNotFoundError:
        return ('Not Found', 404)


if __name__ == "__main__":
    app.run()

# okay decompiling 1071_1.pyc
