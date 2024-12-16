# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 494_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 453 bytes
import zipfile

def extract_and_execute(zip_file):
    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall("/extraction/path")
        exec(open("/extraction/path/some_script.py").read())

# okay decompiling 494_1.pyc
