# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 798_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 540 bytes
import eventlet
from eventlet import wsgi
from eventlet.green import websocket

class MyWebSocketHandler(websocket.WebSocketWSGI):

    def on_message(self, message):
        print("Received message:", message)


def application(environ, start_response):
    if environ["PATH_INFO"] == "/ws":
        return MyWebSocketHandler(environ, start_response)
    start_response("404 Not Found", [])
    return []


wsgi.server(eventlet.listen(('0.0.0.0', 8000)), application)

# okay decompiling 798_1.pyc
