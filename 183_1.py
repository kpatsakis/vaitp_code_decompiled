# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 183_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 517 bytes
import sqlite3

def get_user_details(username):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# okay decompiling 183_1.pyc
