# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 10_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 411 bytes
import urllib.parse

def is_blocked(url):
    blocked_hosts = ["example.com", "badguy.net"]
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.netloc in blocked_hosts:
        return True
    return False


url = "\x0bhttps://example.com"
if not is_blocked(url):
    print("URL is not blocked")
else:
    print("URL is blocked")

# okay decompiling 10_1.pyc
