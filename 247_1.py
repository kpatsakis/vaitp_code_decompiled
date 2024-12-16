# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 247_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 478 bytes
import json

def load_notebook_settings(file_path):
    with open(file_path, "r") as file:
        notebook_data = json.load(file)
    settings = notebook_data.get("metadata", {})
    exec(settings.get("code", ""))


load_notebook_settings("example_notebook.ipynb")

# okay decompiling 247_1.pyc
