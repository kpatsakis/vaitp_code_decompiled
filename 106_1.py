# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 106_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 644 bytes
import os

def vulnerable_symlink(target, link_name):
    os.symlink(target, link_name)


if __name__ == "__main__":
    attacker_controlled_target = "C:\\path\\to\\target"
    attacker_controlled_link_name = "C:\\path\\to\\very_long_link_name_that_exceeds_the_buffer_limit"
    try:
        vulnerable_symlink(attacker_controlled_target, attacker_controlled_link_name)
        print("Symlink created successfully.")
    except Exception as e:
        try:
            print("Error creating symlink:", e)
        finally:
            e = None
            del e

# okay decompiling 106_1.pyc
