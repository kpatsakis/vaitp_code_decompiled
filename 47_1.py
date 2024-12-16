# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 47_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 378 bytes
from PIL import Image
with open("crafted_ycbcr_file.ycbcr", "wb") as f:
    f.write(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\x10\x11\x12\x13\x14\x15')
image = Image.open("crafted_ycbcr_file.ycbcr")
image.load()

# okay decompiling 47_1.pyc
