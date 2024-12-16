# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 44_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 252 bytes
from PIL import Image

def process_pdf(file_path):
    with open(file_path, "rb") as f:
        img = Image.open(f)
        img.load()


process_pdf("crafted_pdf_file.pdf")

# okay decompiling 44_1.pyc
