# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 87_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 340 bytes
from PIL import Image

def process_image(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    img = Image.frombytes("RGB", (1000000, 1000000), image_data)
    img.save("output.png")


process_image("crafted_image_file.png")

# okay decompiling 87_1.pyc
