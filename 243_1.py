# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 243_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 488 bytes
from definitions import load

def vulnerable_load(input_data):
    return load(input_data)


malicious_input = "\nimport os\nos.system('cat /etc/passwd')\n"
vulnerable_load(malicious_input)

# okay decompiling 243_1.pyc
