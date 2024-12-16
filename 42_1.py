# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 42_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 518 bytes
from PIL import Image
from io import BytesIO
blp_data = b'BLP\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01'
blp_data += b'\x00' * (4294967296 - len(blp_data))
img = Image.open(BytesIO(blp_data))
img.load()

# okay decompiling 42_1.pyc
