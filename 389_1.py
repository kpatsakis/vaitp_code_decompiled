# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 389_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 341 bytes


def diffNotebookCheckpoint(file_name):
    notebook_path = file_name + ".ipynb"
    with open(notebook_path, "r") as f:
        notebook_content = f.read()
    return notebook_content


diffNotebookCheckpoint('malicious<script>alert("XSS")</script>')

# okay decompiling 389_1.pyc
