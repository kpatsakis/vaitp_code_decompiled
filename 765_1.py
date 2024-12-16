# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 765_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 604 bytes
import os

def execute_macro(macro_path):
    print(f"Executing macro from: {macro_path}")


def open_document_and_execute_macro(doc_path):
    macro_path = doc_path
    execute_macro(macro_path)


open_document_and_execute_macro("../some/unsafe/path/to/macro.py")

# okay decompiling 765_1.pyc
