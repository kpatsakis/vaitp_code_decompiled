# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 924_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 817 bytes
import re

def install_package(package_name, version):
    package_version = f"{package_name}-{version}"
    if re.match("^[a-zA-Z0-9-_]+-[0-9]+$", package_version):
        print(f"Installing {package_name} version {version}...")
    else:
        print("Invalid package version format.")


install_package("foo", "2-2")

# okay decompiling 924_1.pyc
