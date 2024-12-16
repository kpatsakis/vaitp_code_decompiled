# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 442_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 256 bytes
import tarfile

def extract_tar(tar_path):
    tar = tarfile.open(tar_path)
    for member in tar.getmembers():
        tar.extract(member)

# okay decompiling 442_1.pyc
