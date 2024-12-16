# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 485_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 406 bytes


def allowmodule(module_name):
    return __import__(module_name)


try:
    arbitrary_code = allowmodule("os")
    arbitrary_code.system("echo Vulnerable!")
except ImportError as e:
    try:
        print(e)
    finally:
        e = None
        del e

# okay decompiling 485_1.pyc
