# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 443_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 440 bytes


def increment_metric(metric_name):
    print(f"Incrementing metric: {metric_name}")


def handle_request(request):
    metric_name = request.method
    increment_metric(metric_name)


class Request:

    def __init__(self, method):
        self.method = method


request = Request("GET")
handle_request(request)

# okay decompiling 443_1.pyc
