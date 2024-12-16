# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 246_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 456 bytes
import json

def load_config_vulnerable(config_path):
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
        if "execute" in config_data:
            exec(config_data["execute"])


load_config_vulnerable("path/to/config.json")

# okay decompiling 246_1.pyc
