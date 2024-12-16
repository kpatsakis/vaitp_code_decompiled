# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 80_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 326 bytes
import tarfile
with open("malicious.tar", "wb") as f:
    f.write(b'')
with tarfile.open("malicious.tar", "r") as tar:
    for member in tar:
        print(member.name)

# okay decompiling 80_1.pyc
