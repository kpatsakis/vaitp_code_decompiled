# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 48_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 483 bytes
from PIL import Image

def vulnerable_function(image_data):
    img = Image.frombytes("L", (100, 100), image_data)
    img.show()


malicious_image_data = b'\x00' * 10000
vulnerable_function(malicious_image_data)

# okay decompiling 48_1.pyc
