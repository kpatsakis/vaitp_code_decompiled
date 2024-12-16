# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 965_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 864 bytes
from django.http import HttpResponse
from .models import FileProxy

def get_file(request):
    file_name = request.GET.get("name")
    try:
        file_proxy = FileProxy.objects.get(name=file_name)
        return file_proxy.file.open()
    except:
        except FileProxy.DoesNotExist:
        return         return HttpResponse("File not found.", status=404)


def download_file(request):
    file_name = request.GET.get("name")
    try:
        file_proxy = FileProxy.objects.get(name=file_name)
        response = HttpResponse((file_proxy.file.open()), content_type="application/octet-stream")
        response["Content-Disposition"] = f'attachment; filename="{file_proxy.name}"'
        return response
    except:
        except FileProxy.DoesNotExist:
        return         return HttpResponse("File not found.", status=404)

# okay decompiling 965_1.pyc
