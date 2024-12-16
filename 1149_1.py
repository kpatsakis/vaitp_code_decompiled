# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1149_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 297 bytes


def execute_query(query):
    eval(query)


unsafe_query = "INSERT INTO my_table (column) VALUES ('value'); print('Executed malicious code!')"
execute_query(unsafe_query)

# okay decompiling 1149_1.pyc
