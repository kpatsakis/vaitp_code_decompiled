# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 703_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 569 bytes
from twisted.web.client import RedirectAgent
from twisted.web.http import Headers

class VulnerableRedirectAgent(RedirectAgent):

    def _followRedirect(self, response, request, uri, headers):
        return super()._followRedirect(response, request, uri, headers)


agent = VulnerableRedirectAgent(reactor, contextFactory)
headers = Headers({'cookie':[b'sessionid=abc123'],  'authorization':[b'Bearer token']})
agent.request(b'GET', b'http://example.com/some/resource', headers)

# okay decompiling 703_1.pyc
