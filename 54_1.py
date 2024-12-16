# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 54_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 784 bytes
import urllib.request
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, "http://example.com", "username", "password")
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
url = "http://malicious-server.com/"
request = urllib.request.Request(url)
try:
    response = urllib.request.urlopen(request)
    print(response.read().decode())
except urllib.error.HTTPError as e:
    try:
        print(f"Error: {e.code} {e.reason}")
    finally:
        e = None
        del e

# okay decompiling 54_1.pyc
