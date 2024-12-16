# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1131_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 285 bytes
from ansys.geometry import Geometry

def vulnerable_start_program():
    geometry_service = Geometry()
    geometry_service._start_program()


vulnerable_start_program()

# okay decompiling 1131_1.pyc
