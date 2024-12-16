# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 25_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 390 bytes
from PIL import Image, os

def process_image(image_path):
    temp_file = "temp file.png"
    image = Image.open(image_path)
    image.save(temp_file)
    os.remove(temp_file)


image_path = "example.jpg"
process_image(image_path)

# okay decompiling 25_1.pyc
