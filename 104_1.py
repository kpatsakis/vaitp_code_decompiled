# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 104_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 333 bytes
import ssl
context = ssl.create_default_context()
response = context.wrap_socket().connect(('example.com', 443))
response.sendall(b'GET /%0D%0AHost:%20evil.com HTTP/1.1\r\n\r\n')
print(response.recv(1024))

# okay decompiling 104_1.pyc
