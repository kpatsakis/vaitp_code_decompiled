# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 850_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 687 bytes
from flask import Flask, request, jsonify
app = Flask(__name__)
user_pins = {"user1": "secure_pin"}

@app.route("/api/change_wifi_settings", methods=["POST"])
def change_wifi_settings():
    username = request.json.get("username")
    pin = request.json.get("pin")
    if user_pins.get(username) == pin:
        return jsonify({"success": "Wi-Fi settings changed successfully"})
    return (jsonify({"error": "Unauthorized"}), 403)


if __name__ == "__main__":
    app.run()

# okay decompiling 850_1.pyc
