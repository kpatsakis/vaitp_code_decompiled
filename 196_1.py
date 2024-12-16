# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 196_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 455 bytes
import sys, os
malicious_file = "malicious.py"
with open(malicious_file, "w") as f:
    f.write('print("Malicious code executed!")\n')
sys.argv[0] = "malicious"
sys.path.insert(0, "")
os.execv(sys.executable, [sys.executable] + sys.argv)

# okay decompiling 196_1.pyc
