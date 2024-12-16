# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1128_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 745 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)
users = {"user1": {'password':"old_password",  'active':False}}

@app.route("/api/v1/users/<username>/activate", methods=["POST"])
def activate_user(username):
    if username not in users:
        return (
         jsonify({"error": "User  not found"}), 404)
    data = request.json
    new_password = data.get("new_password")
    if new_password:
        users[username]["active"] = True
        return (jsonify({"message": "User  activated successfully."}), 200)
    return (jsonify({"error": "New password required"}), 400)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 1128_1.pyc
