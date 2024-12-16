# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 311_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 489 bytes
import os, tarfile

def _tar_file(script_parts):
    return [
     "path/to/archive.tar"]


def side_effect(old_cmd, command):
    with tarfile.TarFile(_tar_file(old_cmd.script_parts)[0]) as archive:
        for file in archive.getnames():
            try:
                os.remove(file)
            except OSError:
                pass

# okay decompiling 311_1.pyc
