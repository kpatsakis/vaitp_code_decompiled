# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 553_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 445 bytes
import os

def insecure_install_directory(directory):
    os.makedirs(directory, exist_ok=True)
    os.chmod(directory, 511)
    with open(os.path.join(directory, "sample_file.txt"), "w") as f:
        f.write("This is a sample file.")


insecure_install_directory("/path/to/install/directory")

# okay decompiling 553_1.pyc
