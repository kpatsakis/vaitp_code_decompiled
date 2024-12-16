# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 415_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 235 bytes
import tarfile

def extract_package(package_path, extract_to):
    with tarfile.open(package_path, "r:gz") as tar:
        tar.extractall(path=extract_to)


extract_package("malicious_package.tar.gz", "/safe/directory/")

# okay decompiling 415_1.pyc
