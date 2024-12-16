# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 715_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 653 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route("/<path:path>", methods=["GET"])
def handle_request(path):
    resource = lookup_resource(path)
    if resource is None:
        return (f"Error: Resource '{path}' not found", 404)
    return resource


def lookup_resource(path):
    pass


if __name__ == "__main__":
    app.run()

# okay decompiling 715_1.pyc
