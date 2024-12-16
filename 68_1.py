# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 68_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 313 bytes
from PIL import Image
image = Image.open("image.jpg")
new_size = (10000000, 10000000)
new_image = Image.new("RGB", new_size)
new_image.paste(image, (0, 0))
new_image.save("new_image.jpg")

# okay decompiling 68_1.pyc
