# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 225_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 418 bytes
from pyramid.config import Configurator
from pyramid.response import Response

def static_view(request):
    return Response(body=(open("/path/to/static/index.html", "rb").read()), content_type="text/html")


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("static", "/static/*subpath")
        config.add_view(static_view, route_name="static")
        app = config.make_wsgi_app()

# okay decompiling 225_1.pyc
