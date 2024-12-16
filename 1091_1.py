# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1091_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 268 bytes


def run_script(script):
    exec(script)


malicious_script = "__import__('os').system('whoami')"
run_script(malicious_script)

# okay decompiling 1091_1.pyc
