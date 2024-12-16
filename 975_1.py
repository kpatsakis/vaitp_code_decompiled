# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 975_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 514 bytes
from mod_python import apache

def handler(req):
    query_string = req.args
    if query_string:
        req.write("Query string received: {}".format(query_string))
    else:
        req.write("No query string provided.")
    return apache.OK

# okay decompiling 975_1.pyc
