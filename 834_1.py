# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 834_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 707 bytes
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        user_input = request.form["user_input"]
        return f"Password reset link has been sent to {user_input}"
    return render_template_string('\n        <form method="post">\n            <label for="user_input">Enter your email:</label>\n            <input type="text" id="user_input" name="user_input">\n            <input type="submit" value="Reset Password">\n        </form>\n    ')


if __name__ == "__main__":
    app.run()

# okay decompiling 834_1.pyc
