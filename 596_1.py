# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 596_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 620 bytes
from flask import Flask, request
app = Flask(__name__)
users = {'admin':{"role": "administrator"}, 
 'editor':{"role": "editor"}, 
 'developer':{"role": "developer"}}

@app.route("/admin/user/add", methods=["POST"])
def add_user():
    current_user = request.form.get("current_user")
    new_username = request.form.get("new_username")
    new_role = request.form.get("new_role")
    users[new_username] = {"role": new_role}
    return (f"User  {new_username} added with role {new_role}.", 201)


if __name__ == "__main__":
    app.run()

# okay decompiling 596_1.pyc
