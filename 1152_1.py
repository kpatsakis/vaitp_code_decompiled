# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1152_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 558 bytes
import mysql.connector
connection = mysql.connector.connect(user="your_username",
  password="your_password",
  host="your_host",
  database="your_database")
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")
results = cursor.fetchall()
for row in results:
    print(row)

# okay decompiling 1152_1.pyc
