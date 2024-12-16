# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 156_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 570 bytes


class SetRemoteAddrFromForwardedFor:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
            request.META["REMOTE_ADDR"] = ip.strip()
        response = self.get_response(request)
        return response

# okay decompiling 156_1.pyc
