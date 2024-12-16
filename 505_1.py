# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 505_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 435 bytes
import usd

def load_usd(file_path):
    stage = usd.Stage.Open(file_path)
    for layer in stage.GetRootLayer().GetSubLayers():
        exec(layer.GetSourceUri())
    else:
        return stage


try:
    stage = load_usd("path/to/malicious.usd")
except Exception as e:
    try:
        print(f"Error loading USD file: {e}")
    finally:
        e = None
        del e

# okay decompiling 505_1.pyc
