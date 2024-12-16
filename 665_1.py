# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 665_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 568 bytes
import os

def load_module(module_name):
    module_path = os.path.join("/tmp", module_name)
    if os.path.isfile(module_path):
        exec(open(module_path).read(), globals())
    else:
        raise ImportError(f"Module {module_name} not found in /tmp.")


if __name__ == "__main__":
    try:
        load_module("deployUtil.py")
        load_module("vds_bootstrap.py")
    except ImportError as e:
        try:
            print(e)
        finally:
            e = None
            del e

# okay decompiling 665_1.pyc
