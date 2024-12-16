# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 18_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 514 bytes
import multiprocessing, pickle, os
malicious_pickle = pickle.dumps({"__reduce__": (os.system, ('echo "Vulnerable!" > /tmp/vulnerable', ))})
with multiprocessing.Pool(processes=1, start_method="forkserver") as pool:
    pool.apply_async(pickle.loads, (malicious_pickle,))
print("Vulnerable code executed!")

# okay decompiling 18_1.pyc
