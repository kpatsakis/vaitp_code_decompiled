# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1129_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 466 bytes
from twisted.web import server, resource
from twisted.web.util import redirectTo
from twisted.internet import reactor

class MyResource(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        redirect_url = request.args.get(b'url', [b'/'])[0].decode("utf-8")
        return redirectTo(redirect_url, request)


site = server.Site(MyResource())
reactor.listenTCP(8080, site)
reactor.run()

# okay decompiling 1129_1.pyc
