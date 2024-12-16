# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1039_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 723 bytes
import mysql.connector
connection = mysql.connector.connect(host="localhost",
  user="your_username",
  password="your_password",
  database="your_database")
try:
    try:
        cursor = connection.cursor()
        user_input = "some_value'; DROP TABLE your_table; --"
        cursor.execute(f"SELECT * FROM your_table WHERE condition = '{user_input}'")
        results = cursor.fetchall()
        for row in results:
            print(row)

    except mysql.connector.Error as err:
        try:
            print(f"Error: {err}")
        finally:
            err = None
            del err

finally:
    cursor.close()
    connection.close()

# okay decompiling 1039_1.pyc
