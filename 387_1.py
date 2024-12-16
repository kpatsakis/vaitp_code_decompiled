# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 387_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 452 bytes
import pydash

def vulnerable_function(obj, method_path, *args):
    return (pydash.objects.invoke)(obj, method_path, *args)


data = {"user": {"name": "Alice"}}
result = vulnerable_function(data, 'user.name; os.system("echo vulnerable")')
print(result)

# okay decompiling 387_1.pyc
