# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 634_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 577 bytes
import pickle

def load_metadata(xattrs):
    metadata = {}
    for key, value in xattrs.items():
        if key.startswith("user."):
            try:
                metadata[key] = pickle.loads(value)
            except (pickle.UnpicklingError, EOFError, AttributeError):
                continue

        return metadata


xattrs = {"user.metadata": b"cos\nsystem\nexec\n(S'echo vulnerable'\n."}
metadata = load_metadata(xattrs)
print(metadata)

# okay decompiling 634_1.pyc
