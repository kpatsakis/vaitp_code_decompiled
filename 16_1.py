# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 16_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 434 bytes
from PIL import Image

def process_image(data):
    img = Image.frombytes("RGB", (100, 100), data)
    return img


exploit_data = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff' * 1000000
try:
    process_image(exploit_data)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 16_1.pyc
