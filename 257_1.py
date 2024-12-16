# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 257_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 990 bytes
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor

class MyServerProtocol(WebSocketServerProtocol):

    def onMessage(self, payload, isBinary):
        redirect_url = payload.decode("utf8")
        self.sendMessage(f"Redirecting to: {redirect_url}".encode("utf8"))
        self.sendResponse(302, {"Location": redirect_url})

    def sendResponse(self, status, headers):
        print(f"HTTP/1.1 {status} Found")
        for key, value in headers.items():
            print(f"{key}: {value}")
        else:
            print()


factory = WebSocketServerFactory("ws://localhost:9000")
factory.protocol = MyServerProtocol
reactor.listenTCP(9000, factory)
reactor.run()

# okay decompiling 257_1.pyc
