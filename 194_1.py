# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 194_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 556 bytes


def load_image(image_data):
    width = get_image_width(image_data)
    height = get_image_height(image_data)
    image_buffer_size = width * height * 3
    image_buffer = bytearray(image_buffer_size)
    return image_buffer

# okay decompiling 194_1.pyc
