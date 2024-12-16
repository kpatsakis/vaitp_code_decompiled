# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1096_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 323 bytes
from werkzeug.utils import safe_join
base_path = "C:\\myapp"
unsafe_path = "//server/share"
safe_path = safe_join(base_path, unsafe_path)
print("Safe path:", safe_path)

# okay decompiling 1096_1.pyc
