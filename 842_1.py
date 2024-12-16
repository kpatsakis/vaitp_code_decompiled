# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 842_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 251 bytes
import zipfile

def extract_zip(zip_file_path, extract_to='.'):
    with zipfile.ZipFile(zip_file_path) as zf:
        zf.extractall(extract_to)


extract_zip("malicious.zip", "extracted_files")

# okay decompiling 842_1.pyc
