# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 185_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 321 bytes
import sqlite3

def get_user_details_vulnerable(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# okay decompiling 185_1.pyc
