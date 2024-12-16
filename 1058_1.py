# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1058_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 526 bytes
import zipfile
from pathlib import Path

def vulnerable_zip_path_handling(zip_file_path):
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_path = zipfile.Path(zip_file)
        for name in zip_path.namelist():
            print(name)


vulnerable_zip_path_handling("malicious.zip")

# okay decompiling 1058_1.pyc
