# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 108_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 302 bytes
import zlib
data = b'A' * 1000000 + b'B' * 1000000 + b'C' * 1000000
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)

# okay decompiling 108_1.pyc
