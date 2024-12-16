# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 71_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1109 bytes
import struct
from PIL import Image
pcx_header = b'\xc5PCX'
pcx_header += b'\x01'
pcx_header += b'\x01'
pcx_header += b'\x10\x00'
pcx_header += b'\x10\x00'
pcx_header += b'\x01\x00'
pcx_header += b'\x00\x00'
pcx_header += b'\x00\x00'
pcx_header += b'\x10\x00'
pcx_header += b'\x10\x00'
with open("crafted_pcx.pcx", "wb") as f:
    f.write(pcx_header)
print("Crafted PCX file created: crafted_pcx.pcx")
try:
    img = Image.open("crafted_pcx.pcx")
    print("Pillow opened the crafted PCX file successfully.")
    img.resize((100, 100))
    img.close()
except Exception as e:
    try:
        print("Error: Pillow failed to open or process the crafted PCX file.")
        print(f"Error message: {e}")
    finally:
        e = None
        del e

# okay decompiling 71_1.pyc
