# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 420_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 820 bytes
import tornado.web, tornado.websocket, tornado.ioloop, zlib

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        try:
            decompressed_data = zlib.decompress(message)
            print("Received and decompressed data:", decompressed_data)
        except Exception as e:
            try:
                print("Error processing message:", e)
            finally:
                e = None
                del e

    def on_close(self):
        print("WebSocket closed")


def make_app():
    return tornado.web.Application([
     (
      "/websocket", WebSocketHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# okay decompiling 420_1.pyc
