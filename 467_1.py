# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 467_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 402 bytes
import os, tempfile

def create_temp_file(data):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        try:
            temp_file.write(data.encode())
            temp_file.close()
        except Exception as e:
            try:
                print(f"Error: {e}")
            finally:
                e = None
                del e

    finally:
        os.remove(temp_file.name)

# okay decompiling 467_1.pyc
