# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 31_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 320 bytes
from PIL import Image

def convert_image(image_path):
    image = Image.open(image_path)
    image.convert("RGB")
    return image


image_path = "path/to/image.jpg"
converted_image = convert_image(image_path)

# okay decompiling 31_1.pyc
