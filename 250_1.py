# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 250_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 639 bytes
import mysql.connector

def insecure_database_connection(host, user, password, database):
    try:
        connection = mysql.connector.connect(host=host,
          user=user,
          password=password,
          database=database)
        print("Connection established without SSL.")
        return         return connection
    except mysql.connector.Error as err:
        try:
            print(f"Error: {err}")
        finally:
            err = None
            del err

# okay decompiling 250_1.pyc
