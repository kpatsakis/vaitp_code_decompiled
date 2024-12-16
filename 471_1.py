# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 471_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 313 bytes


def handle_download(file_name, mime_type):
    if mime_type == "text/plain":
        if file_name.endswith(".py"):
            exec(open(file_name).read())
        else:
            open(file_name).read()

# okay decompiling 471_1.pyc
