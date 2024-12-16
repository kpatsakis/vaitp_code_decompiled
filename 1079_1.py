# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1079_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 623 bytes
import zipfile, io
with zipfile.ZipFile("vulnerable.zip", "w") as zf:
    zf.writestr("file1.txt", b'A' * 1000000)
    zf.writestr("file2.txt", b'B' * 1000000)
    zf.writestr("file1.txt", b'A' * 1000000)
with zipfile.ZipFile("vulnerable.zip", "r") as zf:
    print(zf.namelist())
    zf.extractall("extracted_files")

# okay decompiling 1079_1.pyc
