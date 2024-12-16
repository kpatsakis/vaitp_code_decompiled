# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 27_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 243 bytes
from PIL import Image

def vulnerable_code(image_path):
    img = Image.open(image_path)
    path = img.getbbox()
    return path


image_path = "path/to/image.jpg"
vulnerable_code(image_path)

# okay decompiling 27_1.pyc
