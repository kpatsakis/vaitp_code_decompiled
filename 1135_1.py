# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1135_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 435 bytes


class Vanna:

    def ask(self, prompt, visualize=True):
        if visualize:
            exec(prompt)
        else:
            print(f"Input received: {prompt}")


vanna = Vanna()
vanna.ask("print('This is a safe output')")
vanna.ask("import os; os.system('echo Vulnerable!')")

# okay decompiling 1135_1.pyc