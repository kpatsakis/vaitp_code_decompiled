# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 710_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 372 bytes


def set_default_root_password():
    root_password = "!"
    with open("/etc/shadow", "a") as f:
        f.write(f"root:{root_password}:\n")


set_default_root_password()

# okay decompiling 710_1.pyc
