# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 40_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 386 bytes
from PIL import Image
with open("malicious_image.tif", "wb") as f:
    f.write(b'II*\x00\x10\x00\x00\x00\x10\x00\x00\x00\x10\x00\x00\x00\x01\x00\x10\x00')
img = Image.open("malicious_image.tif")
img.load()

# okay decompiling 40_1.pyc
