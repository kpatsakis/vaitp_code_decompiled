# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 590_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 331 bytes
import bpy

def vulnerable_script_link():
    exec("print('Executing arbitrary code!')")


bpy.app.handlers.load_post.append(vulnerable_script_link)

# okay decompiling 590_1.pyc
