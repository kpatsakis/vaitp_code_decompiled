# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 926_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 992 bytes
import socket, requests

class WireMockProxy:

    def __init__(self, allowed_domains):
        self.allowed_domains = allowed_domains

    def is_domain_allowed(self, domain):
        return domain in self.allowed_domains

    def proxy_request(self, target_domain, request_data):
        if not self.is_domain_allowed(target_domain):
            raise ValueError("Domain not allowed for proxying")
        target_ip = socket.gethostbyname(target_domain)
        response = requests.post(f"http://{target_ip}/proxy", json=request_data)
        return response


allowed_domains = [
 "example.com", "api.example.com"]
proxy = WireMockProxy(allowed_domains)
try:
    response = proxy.proxy_request("example.com", {"key": "value"})
    print(response.json())
except ValueError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 926_1.pyc
