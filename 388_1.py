# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 388_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 480 bytes
import os, random

def move_faqwiz(source, destination):
    temp_file_path = f"tmp{random.randint(1, 100000)}.tmp"
    with open(temp_file_path, "wb") as temp_file:
        with open(source, "rb") as src_file:
            data = src_file.read()
            temp_file.write(data)
    os.rename(temp_file_path, destination)

# okay decompiling 388_1.pyc
