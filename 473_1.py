# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 473_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 611 bytes
from twisted.web.client import Agent
from twisted.web.http import ResponseDone
from twisted.internet import reactor

class MyAgent(Agent):

    def __init__(self, reactor, trustRoot=None):
        super(MyAgent, self).__init__(reactor, trustRoot)

    def get(self, url):
        d = self.request(b'GET', url)
        d.addCallback(self.handle_response)
        return d

    def handle_response(self, response):
        print("Response received:", response)
        return response


agent = MyAgent(reactor)
agent.get("https://untrusted-server.com/resource")
reactor.run()

# okay decompiling 473_1.pyc
