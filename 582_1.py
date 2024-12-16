# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 582_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 312 bytes
import zlib

def vulnerable_file_compress(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        compressed_data = zlib.compress(data)
    return compressed_data


compressed = vulnerable_file_compress("path/to/input/file")

# okay decompiling 582_1.pyc
