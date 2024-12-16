# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1120_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 472 bytes
import os

def upload_template(user, template_path, upload_folder):
    print(f"Uploading template from {template_path} to {upload_folder}")


upload_template("authenticated_user", "template.py", "/some/unsafe/directory")

# okay decompiling 1120_1.pyc
