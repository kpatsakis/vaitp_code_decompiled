# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 820_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 328 bytes
from twisted.web import server, resource

class MyResource(resource.Resource):
    isLeaf = True

    def render(self, request):
        return b'Hello, world!'


site = server.Site(MyResource())
from twisted.internet import reactor
reactor.listenTCP(8080, site)
reactor.run()

# okay decompiling 820_1.pyc
