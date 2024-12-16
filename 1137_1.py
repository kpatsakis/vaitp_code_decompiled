# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1137_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 474 bytes


def execute_query(db_connection, query):
    if "INSERT" in query:
        eval(query)
    else:
        raise ValueError("Invalid query type")


conn = None
execute_query(conn, "INSERT INTO users (name) VALUES ('Alice'); os.system('whoami')")

# okay decompiling 1137_1.pyc
