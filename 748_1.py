# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 748_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 364 bytes
import rrdtool

def vulnerable_graph(filename, title, data):
    rrdtool.graph(filename, title=title,
      data=data)


vulnerable_graph("output.png", "Sample Graph", "Data: %s" % "Sample data")

# okay decompiling 748_1.pyc
