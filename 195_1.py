# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 195_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 313 bytes
from PIL import Image
img = Image.new("RGB", (1, 1), (255, 255, 255))
zsize = 268435456
img.save("vulnerable_image.bmp", "BMP", zsize=zsize)

# okay decompiling 195_1.pyc
