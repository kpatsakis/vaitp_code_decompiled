# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 606_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 468 bytes


def import_bvh(file_path):
    with open(file_path, "r") as file:
        hierarchy_element = file.read()
        try:
            result = eval(hierarchy_element)
        except Exception as e:
            try:
                print(f"Error processing the hierarchy element: {e}")
            finally:
                e = None
                del e

# okay decompiling 606_1.pyc
