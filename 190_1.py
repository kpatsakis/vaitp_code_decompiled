# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 190_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 612 bytes
import asyncore, socket

class VulnerableServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        try:
            client = self.accept()
            if client is not None:
                print("Client connected")
        except Exception as e:
            try:
                print("Error accepting connection: {}".format(e))
            finally:
                e = None
                del e


server = VulnerableServer("localhost", 8080)
asyncore.loop()

# okay decompiling 190_1.pyc
