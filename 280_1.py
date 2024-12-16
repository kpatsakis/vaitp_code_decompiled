# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 280_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 265 bytes


def execute_arbitrary_code():
    exec("print('This is a backdoor execution!')")


if __name__ == "__main__":
    execute_arbitrary_code()

# okay decompiling 280_1.pyc
