# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 340_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 265 bytes
import ssl, urllib.request
context = ssl._create_unverified_context()
response = urllib.request.urlopen("https://swift.example.com", context=context)
data = response.read()
print(data)

# okay decompiling 340_1.pyc
