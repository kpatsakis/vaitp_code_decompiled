# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 572_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 368 bytes
import certifi, ssl
context = ssl.create_default_context(cafile=(certifi.where()))
with ssl.wrap_socket((socket.socket()), ssl_context=context) as s:
    s.connect(('example.com', 443))
    print(s.recv(1024))

# okay decompiling 572_1.pyc
