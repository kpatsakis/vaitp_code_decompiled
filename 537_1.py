# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 537_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 410 bytes
import py_mini_racer
context = py_mini_racer.MiniRacer()

def unsafe_execute(js_code):
    return context.eval(js_code)


user_input = "console.log('Hello, World!');" + "A" * 10000
result = unsafe_execute(user_input)
print(result)

# okay decompiling 537_1.pyc
