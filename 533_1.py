# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 533_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 239 bytes


def unsafe_json_eval(data):
    return eval(data)


json_data = '{"key": "__import__(\'os\').system(\'ls\')"}'
parsed_data = unsafe_json_eval(json_data)
print(parsed_data)

# okay decompiling 533_1.pyc
