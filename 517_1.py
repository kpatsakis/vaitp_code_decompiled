# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 517_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 468 bytes
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class InteractiveConsoleHandler(webapp.RequestHandler):

    def post(self):
        code = self.request.get("code")
        exec(code)


app = webapp.WSGIApplication([
 (
  "/_ah/admin/interactive/execute", InteractiveConsoleHandler)],
  debug=True)

def main():
    util.run_wsgi_app(app)


if __name__ == "__main__":
    main()

# okay decompiling 517_1.pyc
