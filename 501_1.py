# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 501_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 349 bytes
import os, sys

def load_module(module_name):
    return __import__(module_name)


my_module = load_module("my_trojan_module")

# okay decompiling 501_1.pyc
