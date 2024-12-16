# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1022_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 437 bytes
import mimetypes

def handle_uploaded_file(file):
    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type.startswith("text/"):
        with open(file.filename, "r") as f:
            content = f.read()
            exec(content)
    else:
        print("Unsupported file type.")

# okay decompiling 1022_1.pyc
