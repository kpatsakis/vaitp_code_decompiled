# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1084_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 364 bytes
import os

def create_shared_environment(env_path):
    os.makedirs(env_path, exist_ok=True)
    os.chmod(env_path, 511)


create_shared_environment("/path/to/shared/python/environment")

# okay decompiling 1084_1.pyc
