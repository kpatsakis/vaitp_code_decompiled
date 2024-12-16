# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 413_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 246 bytes
import shutil

def extract_package(package_path, target_directory):
    shutil.unpack_archive(package_path, target_directory)


extract_package("malicious_package.zip", "/path/to/target/directory")

# okay decompiling 413_1.pyc
