# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 58_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 359 bytes
from PIL import Image
with open("crafted_tiff.tif", "wb") as f:
    f.write(b'II*\x00\x10\x00\x00\x00\x11\x00\x12\x00\x13\x00\x14\x00\x15\x00\x16\x00\x17\x00\x18\x00\x19\x00\x1a\x00')
img = Image.open("crafted_tiff.tif")
img.load()

# okay decompiling 58_1.pyc
