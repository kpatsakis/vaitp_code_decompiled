# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 801_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 596 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/set_theme", methods=["POST"])
def set_theme():
    new_theme_name = request.form.get("newThemeName")
    execute_theme_change(new_theme_name)


def execute_theme_change(theme_name):
    eval(theme_name)


if __name__ == "__main__":
    app.run()

# okay decompiling 801_1.pyc
