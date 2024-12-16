# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 49_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 354 bytes
from PIL import Image
with open("malicious.jp2", "wb") as f:
    f.write(b'\x00\x00\x00\x0cjP  \r\n\x87\n')
img = Image.open("malicious.jp2")
img.verify()

# okay decompiling 49_1.pyc
