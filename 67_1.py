# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 67_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 327 bytes
from PIL import Image

def parse_sgi_image(file_path):
    with open(file_path, "rb") as f:
        image_data = f.read()
    img = Image.frombytes("L", ((image_data[0] << 16) + image_data[1]), (image_data[2[:None]]), decoder_name="sgi_rle")
    return img


sgi_image_path = "example.sgi"
parse_sgi_image(sgi_image_path)

# okay decompiling 67_1.pyc
