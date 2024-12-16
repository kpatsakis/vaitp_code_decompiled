# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 57_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 303 bytes
from PIL import Image
with open("crafted_sgi_rle_image.sgi", "rb") as f:
    image_data = f.read()
image = Image.frombytes("L", (100, 100), image_data)
image.show()

# okay decompiling 57_1.pyc
