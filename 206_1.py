# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 206_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 391 bytes
import imageop

def vulnerable_image_processing(image_data):
    processed_image = imageop.some_image_operation(image_data)
    return processed_image


crafted_image_data = b'\x00' * 4294967296
vulnerable_image_processing(crafted_image_data)

# okay decompiling 206_1.pyc
