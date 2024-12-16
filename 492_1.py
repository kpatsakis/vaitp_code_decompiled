# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 492_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 378 bytes
import yaml

def vulnerable_load_yaml(vault_content):
    return yaml.load(vault_content, Loader=(yaml.FullLoader))


vault_content = "\nmy_secret: !!python/object/apply:os.system ['echo vulnerable']\n"
data = vulnerable_load_yaml(vault_content)
print(data)

# okay decompiling 492_1.pyc
