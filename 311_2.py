# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 311_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 466 bytes
import os, zipfile

def _zip_file(old_cmd):
    return "path/to/archive.zip"


def side_effect(old_cmd, command):
    with zipfile.ZipFile(_zip_file(old_cmd), "r") as archive:
        for file in archive.namelist():
            try:
                os.remove(file)
            except OSError:
                pass

# okay decompiling 311_2.pyc
