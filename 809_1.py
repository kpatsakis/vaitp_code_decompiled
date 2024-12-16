# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 809_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 464 bytes
import os

def create_jsnapy_config(directory):
    os.makedirs(directory, mode=511)
    config_file_path = os.path.join(directory, "sample_config.yml")
    with open(config_file_path, "w") as config_file:
        config_file.write("sample_config: value\n")


create_jsnapy_config("/path/to/jsnapy/config")

# okay decompiling 809_1.pyc
