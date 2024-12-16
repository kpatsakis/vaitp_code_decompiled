# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 37_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 309 bytes
from PIL import Image

def load_image(file_path):
    try:
        img = Image.open(file_path)
        img.load()
    except Exception as e:
        try:
            print(f"Error loading image: {e}")
        finally:
            e = None
            del e


load_image("malicious_image.fli")

# okay decompiling 37_1.pyc
