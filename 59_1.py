# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 59_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 268 bytes
from PIL import Image

def process_pcx_file(file_path):
    with open(file_path, "rb") as f:
        pcx_data = f.read()
    img = Image.frombytes("RGB", (100, 100), pcx_data)
    img.show()


process_pcx_file("crafted_pcx_file.pcx")

# okay decompiling 59_1.pyc
