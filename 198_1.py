# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 198_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 428 bytes
from PIL import Image

def vulnerable_crop(image, box):
    left, upper, right, lower = box
    return image.crop(box)


if __name__ == "__main__":
    img = Image.open("example.jpg")
    crop_box = (0, 0, 1000000000, 1000000000)
    cropped_image = vulnerable_crop(img, crop_box)
    cropped_image.show()

# okay decompiling 198_1.pyc
