# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1182_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 301 bytes
import subprocess

def vulnerable_install(package_name):
    subprocess.run(["pip", "install", package_name], check=True)


vulnerable_install("malicious-package")

# okay decompiling 1182_1.pyc
