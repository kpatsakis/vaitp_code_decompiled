# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 474_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 426 bytes
import requests
from requests_kerberos import HTTPKerberosAuth
kerberos_auth = HTTPKerberosAuth(mutual_authentication=(HTTPKerberosAuth.OPTIONAL))
response = requests.get("http://example.com/protected", auth=kerberos_auth)
if response.status_code == 200:
    print("Access granted")
else:
    print("Access denied")

# okay decompiling 474_1.pyc
