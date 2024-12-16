# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 618_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 720 bytes
import os, json

def load_repository(repository_path):
    roles = {}
    for filename in os.listdir(repository_path):
        if filename.endswith(".json"):
            role_name = os.path.splitext(filename)[0]
            with open(os.path.join(repository_path, filename), "r") as f:
                roles[role_name] = json.load(f)
            with open(f"{role_name}.json", "w") as f:
                json.dump(roles[role_name], f)
        return roles


repository = load_repository("/path/to/repository")

# okay decompiling 618_1.pyc
