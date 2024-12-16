# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 563_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 311 bytes
import numpy as np

def vulnerable_load(file_path):
    return np.load(file_path, allow_pickle=True)

# okay decompiling 563_1.pyc
