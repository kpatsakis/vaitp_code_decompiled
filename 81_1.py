# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 81_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 730 bytes
from PIL import Image

def vulnerable_function(image_path):
    try:
        with open(image_path, "rb") as image_file:
            image = Image.open(image_file)
            num_bands = image.im.bands
            range(num_bands)
            image.load()
    except Exception as e:
        try:
            print(f"An error occurred: {e}")
        finally:
            e = None
            del e


vulnerable_function("example_image.jpg")

# okay decompiling 81_1.pyc
