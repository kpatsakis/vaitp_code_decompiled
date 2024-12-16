# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 810_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 564 bytes


def render_document_tree_macro(params):
    """
    Render the document tree macro with potentially unsafe parameters.
    This function does not escape parameters, leading to a vulnerability.
    """
    output = f"<div class='document-tree'>{params}</div>"
    return output


params = {'param1':"value1", 
 'param2':"{malicious_code}"}
vulnerable_output = render_document_tree_macro(params)
print(vulnerable_output)

# okay decompiling 810_1.pyc
