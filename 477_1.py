# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 477_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 404 bytes
import subprocess

def change_owner(path, user):
    subprocess.run(["chown", user, path])


def setup_dropbear():
    target_path = "/etc/init.d/S50dropbear.sh"
    change_owner(target_path, "python")


setup_dropbear()

# okay decompiling 477_1.pyc
