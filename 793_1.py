# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 793_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 536 bytes
from tuf import repository_tool

def download_root_metadata(repository):
    root_metadata = repository.get_root()
    print("Root metadata downloaded and trusted without verification.")
    return root_metadata


repository = repository_tool.create_new_repository("repository_path")
downloaded_root = download_root_metadata(repository)

# okay decompiling 793_1.pyc
