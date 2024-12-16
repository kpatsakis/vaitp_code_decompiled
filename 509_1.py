# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 509_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 358 bytes
import pickle

def load_pickle(data):
    return pickle.loads(data)


if __name__ == "__main__":
    with open("data.pkl", "rb") as f:
        data = f.read()
        obj = load_pickle(data)
        print("Loaded object:", obj)

# okay decompiling 509_1.pyc
