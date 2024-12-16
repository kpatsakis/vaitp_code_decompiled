# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 514_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 744 bytes
import os

def execute_python_version():
    current_directory = os.getcwd()
    version_file_path = os.path.join(current_directory, ".python-version")
    if os.path.exists(version_file_path):
        with open(version_file_path, "r") as f:
            version = f.read().strip()
            pyenv_root = os.path.expanduser("~/.pyenv")
            version_path = os.path.join(pyenv_root, "versions", version)
            if os.path.isfile(version_path):
                os.system(version_path)
            else:
                print(f"Python version {version} not found.")


execute_python_version()

# okay decompiling 514_1.pyc
