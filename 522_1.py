# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 522_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 731 bytes
from plone.dexterity.content import Container

class VulnerableTraceback(Container):

    def get_traceback(self, request):
        if request.authenticated_user.has_role("Manager"):
            url = request.get("url", "")
            response = self.make_request_to_url(url)
            return response
        raise PermissionError("You do not have permission to view tracebacks.")

    def make_request_to_url(self, url):
        import requests
        return requests.get(url).text

# okay decompiling 522_1.pyc
