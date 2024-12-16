# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 349_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 351 bytes
from flask import Flask
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on("connect")
def handle_connect():
    print("Client connected")


if __name__ == "__main__":
    socketio.run(app)

# okay decompiling 349_1.pyc
