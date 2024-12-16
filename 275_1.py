# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 275_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 147 bytes
import rrdtool

def generate_graph(title, output_file):
    rrdtool.graph(output_file, f"--title={title}")

# okay decompiling 275_1.pyc
