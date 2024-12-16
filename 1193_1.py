# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1193_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 592 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)
users = {1:{'name':"Alice", 
  'email':"alice@example.com"}, 
 2:{'name':"Bob", 
  'email':"bob@example.com"}}

@app.route("/api/myapp/index/user/info", methods=["GET"])
def get_user_info():
    user_id = request.args.get("id")
    user_info = users.get(int(user_id))
    if user_info:
        return jsonify(user_info)
    return (jsonify({"error": "User  not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# okay decompiling 1193_1.pyc
