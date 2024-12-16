# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 874_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 753 bytes
import mysql.connector

def vulnerable_connect():
    try:
        try:
            connection = mysql.connector.connect(host="localhost",
              user="your_username",
              password="your_password",
              database="your_database")
            if connection.is_connected():
                print("Successfully connected to the database")
        except mysql.connector.Error as e:
            try:
                print(f"Error: {e}")
            finally:
                e = None
                del e

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed")


vulnerable_connect()

# okay decompiling 874_1.pyc
