# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 15_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 464 bytes
from PIL import Image
img = Image.open("image.tif")
tag_data = img.tag[270]
malicious_tag_data = b'\x00' * 1048576
img.tag[270] = malicious_tag_data
img.save("output.tif")

# okay decompiling 15_1.pyc
