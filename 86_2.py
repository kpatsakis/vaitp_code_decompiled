# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 86_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 625 bytes
import glob
files = glob.glob("*.txt")
with open("output.txt", "w") as output:
    for file in files:
        with open(file, "r") as input:
            output.write(input.read())

# okay decompiling 86_2.pyc