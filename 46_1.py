# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 46_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 526 bytes
from PIL import Image
ifd = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19 ')
ifd += b'\x00\x00\x00\x00'
ifd += b'\x00\x00\x00\x10'
image = Image.frombytes("I;16", (100, 100), ifd)
image.load()

# okay decompiling 46_1.pyc
