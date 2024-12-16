# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 731_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 414 bytes
import urllib.parse, os

def execute_script(encoded_script_path):
    script_path = urllib.parse.unquote(encoded_script_path)
    exec(open(script_path).read())

# okay decompiling 731_1.pyc
