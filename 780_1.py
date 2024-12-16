# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 780_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 564 bytes


def vulnerable_mcopy(src, dest):
    """
    A vulnerable copy function that does not properly restrict the length of the source string.
    
    Args:
        src (str): The source string to copy from.
        dest (list): The destination list to copy to (simulating a buffer).
    """
    dest.clear()
    dest.extend(src)


destination_buffer = []
vulnerable_mcopy("A crafted string that could potentially cause issues" * 100, destination_buffer)

# okay decompiling 780_1.pyc
