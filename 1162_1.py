# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1162_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 220 bytes


def filter_view(request):
    user_input = request.GET.get("filter_param", "")
    response = f"<div>User input: {user_input}</div>"
    return HttpResponse(response)

# okay decompiling 1162_1.pyc
