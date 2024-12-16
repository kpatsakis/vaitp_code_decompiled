# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1018_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 603 bytes
import tornado.web, tornado.websocket, json

class VulnerableWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        data = json.loads(message)

    def on_close(self):
        print("WebSocket closed")


application = tornado.web.Application([
 (
  "/websocket", VulnerableWebSocket)])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# okay decompiling 1018_1.pyc
