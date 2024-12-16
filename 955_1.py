# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 955_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 390 bytes
import subprocess, os

def run_git_command(command, repo_path):
    os.chdir(repo_path)
    result = subprocess.run(command, shell=True, check=True, capture_output=True)
    return result.stdout

# okay decompiling 955_1.pyc
