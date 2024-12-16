# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 410_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 595 bytes
from nbconvert import HTMLExporter

def convert_notebook_to_html(notebook_content):
    exporter = HTMLExporter()
    html_output, _ = exporter.from_notebook_node(notebook_content)
    return html_output


notebook_content = {"cells": [
           {'cell_type':"code", 
            'source':'print("<script>alert(\'XSS Attack!\')</script>")'}]}
html_output = convert_notebook_to_html(notebook_content)
print(html_output)

# okay decompiling 410_1.pyc
