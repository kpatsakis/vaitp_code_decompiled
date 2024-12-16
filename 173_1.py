# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 173_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 476 bytes
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def vulnerable_view(request):
    file_path = request.GET.get("file_path")
    file_data = open(file_path, "r").read()
    return HttpResponse(file_data, content_type="text/plain")

# okay decompiling 173_1.pyc
