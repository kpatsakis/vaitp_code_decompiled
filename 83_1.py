# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 83_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 460 bytes
import ast
import typed_ast.ast3 as typed_ast

def vulnerable_function(source_code):
    tree = ast.parse(source_code)
    typed_tree = typed_ast.ast_to_typed_ast(tree)
    typed_tree.body[0].value.numerator.numerator


vulnerable_function("x = 1")

# okay decompiling 83_1.pyc
