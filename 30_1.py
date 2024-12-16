# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 30_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 376 bytes
import pybluemonday
policy = pybluemonday.UGCPolicy()
input = "<select><option>option1</option><option>option2</option><style>/* malicious CSS */</style></select>"
sanitized = policy.sanitize(input)
print(sanitized)

# okay decompiling 30_1.pyc
