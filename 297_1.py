# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 297_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 330 bytes
import democritus_strings

def execute_vulnerable_function():
    democritus_strings.execute_malicious_code()


execute_vulnerable_function()

# okay decompiling 297_1.pyc
