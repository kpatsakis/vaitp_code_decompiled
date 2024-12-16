# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 573_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 728 bytes
import os, subprocess

def insecure_sudo_configuration():
    sudoers_file = "/etc/sudoers"
    backup_file = "/etc/sudoers.bak"
    subprocess.run(["cp", sudoers_file, backup_file])
    os.chmod(sudoers_file, 420)
    with open(sudoers_file, "a") as f:
        f.write("\n# Insecure sudoers configuration\n")
        f.write("Defaults    !secure_path\n")
        f.write("Defaults    env_reset\n")
        f.write("Defaults    visiblepw\n")


insecure_sudo_configuration()

# okay decompiling 573_1.pyc
