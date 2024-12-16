# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 496_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 578 bytes


class Togglee:

    def __init__(self):
        self.settings = {}

    def set_setting(self, key, value):
        self.settings[key] = value

    def execute_code(self, code):
        exec(code)


togglee = Togglee()
togglee.set_setting("setting1", "value1")
togglee.execute_code('import os; os.system("echo Vulnerable!")')

# okay decompiling 496_1.pyc
