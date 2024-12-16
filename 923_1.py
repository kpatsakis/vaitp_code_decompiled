# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 923_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 356 bytes
import os

class Snippets:

    def __init__(self, base_path):
        self.base_path = os.path.abspath(base_path)

    def get_snippet_path(self, path):
        full_path = os.path.join(self.base_path, path)
        return full_path

# okay decompiling 923_1.pyc
