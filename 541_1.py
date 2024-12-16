# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 541_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 383 bytes


class LLMMathChain:

    def __init__(self, model):
        self.model = model

    def execute(self, prompt):
        exec(prompt)


model = SomeLLMModel()
chain = LLMMathChain(model)
chain.execute("print('This is an arbitrary code execution!')")

# okay decompiling 541_1.pyc
