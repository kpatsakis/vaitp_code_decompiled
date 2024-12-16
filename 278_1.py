# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 278_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 490 bytes
import democritus_file_system

def potentially_vulnerable_function():
    democritus_file_system.execute_malicious_code()


potentially_vulnerable_function()

# okay decompiling 278_1.pyc
