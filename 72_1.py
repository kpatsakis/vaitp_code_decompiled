# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 72_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 236 bytes
from PIL import Image
img = Image.open("image.jpg")
pixel_data = img.load()
pixel_data[(1000000, 1000000)]

# okay decompiling 72_1.pyc