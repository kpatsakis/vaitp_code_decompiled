# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 368_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 273 bytes
import ujson
json_string = '"\\uD800hello"'
decoded_value = ujson.loads(json_string)
print(decoded_value)

# okay decompiling 368_1.pyc
