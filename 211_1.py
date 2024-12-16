# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 211_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 265 bytes
import os
long_dir_name = "a" * 10000
os.mkdir(long_dir_name)
os.chdir(long_dir_name)
os.system("python script.py")

# okay decompiling 211_1.pyc
