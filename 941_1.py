# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 941_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 415 bytes
from PIL import Image, ImageDraw, ImageFont

def vulnerable_draw_text(image, text, position, font):
    draw = ImageDraw.Draw(image)
    draw.text(position, text, font=font)


image = Image.new("RGB", (200, 100), color="white")
font = ImageFont.load_default()
vulnerable_draw_text(image, "A" * 10000, (10, 10), font)

# okay decompiling 941_1.pyc
