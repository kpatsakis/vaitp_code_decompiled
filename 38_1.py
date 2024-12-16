# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 38_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 480 bytes
from PIL import Image

def vulnerable_code(image_path):
    try:
        img = Image.open(image_path)
        img.load()
        print("Image loaded successfully")
    except Exception as e:
        try:
            print(f"Error: {e}")
        finally:
            e = None
            del e


image_path = "example.psd"
vulnerable_code(image_path)

# okay decompiling 38_1.pyc
