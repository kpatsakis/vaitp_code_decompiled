# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 593_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 528 bytes


class PALChain:

    def __init__(self):
        pass

    def from_math_prompt(self, prompt):
        exec(f"result = {prompt}")
        return result

    def from_colored_object_prompt(self, prompt):
        exec(f"result = {prompt}")
        return result


chain = PALChain()
result = chain.from_math_prompt("os.system('echo Vulnerable')")
print(result)

# okay decompiling 593_1.pyc
