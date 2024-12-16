# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1148_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 557 bytes
from RestrictedPython import compile_restricted
from RestrictedPython.Utilities import utility_builtins
code = "result = string.ascii_letters"
compiled_code = compile_restricted(code, "<string>", "exec")
namespace = {}
exec(compiled_code, namespace)
print(namespace["result"])

# okay decompiling 1148_1.pyc
