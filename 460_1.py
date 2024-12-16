# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 460_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1130 bytes
import json

def load_notebook(file_path):
    with open(file_path, "r") as f:
        notebook_content = json.load(f)
    exec(notebook_content["cells"][0]["source"])


load_notebook("malicious_notebook.ipynb")

# okay decompiling 460_1.pyc
