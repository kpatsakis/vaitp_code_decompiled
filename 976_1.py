# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 976_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 359 bytes
from mod_python import apache

def handler(req):
    query_string = req.args
    req.write("Processing query string: " + query_string)
    return apache.OK

# okay decompiling 976_1.pyc
