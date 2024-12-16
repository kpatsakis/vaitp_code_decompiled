# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 43_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 324 bytes
from PIL import Image
with open("malicious.sgi", "wb") as f:
    f.write(b'\x01\x01\x01\x01')
img = Image.open("malicious.sgi")
img.load()

# okay decompiling 43_1.pyc
