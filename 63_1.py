# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 63_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 530 bytes
import importlib, sys

def load_module(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            module = importlib.util.module_from_spec(spec)
            spec.loader.load_module(module)
            return             return module
        raise ImportError(f"Module {module_name} not found.")
    except Exception as e:
        try:
            print(f"Error loading module {module_name}: {e}")
        finally:
            e = None
            del e


if __name__ == "__main__":
    module_name = sys.argv[1]
    load_module(module_name)

# okay decompiling 63_1.pyc
