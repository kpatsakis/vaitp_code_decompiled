# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 207_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 276 bytes
from imageop import crop
from PIL import Image
image = Image.new("RGB", (1000, 1000))
cropped_image = crop(image, (0, 0, 1001, 1001))

# okay decompiling 207_1.pyc
