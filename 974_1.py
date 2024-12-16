# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 974_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 979 bytes
import os, stat

def insecure_permissions(python_directory):
    for root, dirs, files in os.walk(python_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            os.chmod(dir_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)

    else:
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)


insecure_permissions("C:\\Python311")

# okay decompiling 974_1.pyc
