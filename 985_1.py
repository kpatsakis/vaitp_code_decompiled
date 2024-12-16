# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 985_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 369 bytes
import os

def vulnerable_walk(top):
    """A function that demonstrates the vulnerability by using os.walk(), which can hit recursion limits."""
    for dirpath, dirnames, filenames in os.walk(top):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            print(full_path)


vulnerable_walk("/path/to/scan")

# okay decompiling 985_1.pyc
