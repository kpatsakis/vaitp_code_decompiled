# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1075_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 394 bytes
from urllib.parse import urlparse, urlsplit
url = "http://[not-an-ipv6]:8080/path"
parsed_url = urlparse(url)
print("Parsed URL:", parsed_url)
if parsed_url.hostname:
    print("Hostname:", parsed_url.hostname)
else:
    print("No valid hostname found.")

# okay decompiling 1075_1.pyc
