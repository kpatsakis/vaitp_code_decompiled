# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 193_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 344 bytes
import rgbimg
malicious_image = b'\x01\x02\x03\x04'
img = rgbimg.rgbimg()
img.longimagedata(malicious_image)

# okay decompiling 193_1.pyc
