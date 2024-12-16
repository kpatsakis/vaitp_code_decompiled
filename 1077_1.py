# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1077_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 959 bytes
import tempfile, os, stat
with tempfile.TemporaryDirectory() as temp_dir:
    target_file = os.path.join(temp_dir, "target_file.txt")
    with open(target_file, "w") as f:
        f.write("This is a target file.")
    symlink_path = os.path.join(temp_dir, "symlink_to_target")
    os.symlink(target_file, symlink_path)
    os.chmod(target_file, stat.S_IRUSR)
    try:
        os.remove(symlink_path)
    except Exception as e:
        try:
            print(f"Error during cleanup: {e}")
        finally:
            e = None
            del e

# okay decompiling 1077_1.pyc
