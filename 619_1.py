# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 619_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 303 bytes
import subprocess

def clone_repository(repo_url):
    command = f"git clone {repo_url}"
    subprocess.run(command, shell=True)


clone_repository("https://example.com/repo.git; rm -rf /")

# okay decompiling 619_1.pyc
