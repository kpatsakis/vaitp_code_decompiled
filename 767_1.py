# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 767_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 396 bytes
import os

def get_package_hook(package_name):
    hook_path = os.path.join("/usr/share/apport/package-hooks/", package_name + ".py")
    if os.path.isfile(hook_path):
        with open(hook_path) as hook_file:
            exec(hook_file.read())
    else:
        raise FileNotFoundError(f"Hook file for package {package_name} not found.")

# okay decompiling 767_1.pyc
