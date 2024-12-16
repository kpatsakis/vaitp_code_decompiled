# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 833_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 473 bytes


def execute_macro(user, macro_code):
    exec(macro_code)


user = get_current_user()
macro_input = "import os; os.system('echo Vulnerable!')"
execute_macro(user, macro_input)

# okay decompiling 833_1.pyc
