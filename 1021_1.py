# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1021_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 937 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/fcopydir", methods=["POST"])
@app.route("/fmkdir", methods=["POST"])
@app.route("/frmdir", methods=["POST"])
@app.route("/getenv", methods=["GET"])
@app.route("/dumpenv", methods=["GET"])
@app.route("/fcopy", methods=["POST"])
@app.route("/fput", methods=["POST"])
@app.route("/fdel", methods=["POST"])
@app.route("/fmove", methods=["POST"])
@app.route("/fget", methods=["GET"])
@app.route("/fappend", methods=["POST"])
@app.route("/fdir", methods=["GET"])
@app.route("/getTraces", methods=["GET"])
@app.route("/kill", methods=["POST"])
@app.route("/pexec", methods=["POST"])
@app.route("/stop", methods=["POST"])
@app.route("/pythonexec", methods=["POST"])
def handle_request():
    return ('Request processed', 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# okay decompiling 1021_1.pyc
