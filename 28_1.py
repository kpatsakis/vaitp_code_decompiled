# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 28_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 429 bytes
from PIL import Image, ImagePath

def vulnerable_function(image_data):
    path = ImagePath.Path(image_data)
    bbox = path.getbbox()
    return bbox


image_data = b'...'
result = vulnerable_function(image_data)
print(result)

# okay decompiling 28_1.pyc
