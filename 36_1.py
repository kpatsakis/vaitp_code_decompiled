# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 36_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1432 bytes
from PIL import Image

def open_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
    except Exception as e:
        try:
            print(f"Error opening image: {e}")
        finally:
            e = None
            del e


open_image("vulnerable_eps_file.eps")

# okay decompiling 36_1.pyc
