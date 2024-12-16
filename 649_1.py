# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 649_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 557 bytes
import pickle

def load_metadata(metadata):
    return pickle.loads(metadata)


def save_metadata(metadata):
    return pickle.dumps(metadata)


metadata_to_save = {'key':"value", 
 'another_key':123}
serialized_metadata = save_metadata(metadata_to_save)
loaded_metadata = load_metadata(serialized_metadata)
print(loaded_metadata)

# okay decompiling 649_1.pyc
