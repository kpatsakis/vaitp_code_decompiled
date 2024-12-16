# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 769_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 700 bytes


def read_pyc(file_path):
    with open(file_path, "rb") as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code_length = f.read(4)
        code_length = int.from_bytes(code_length, byteorder="little")
        code_data = f.read(code_length)
        process_code_object(code_data)


def process_code_object(code_data):
    pass

# okay decompiling 769_1.pyc
