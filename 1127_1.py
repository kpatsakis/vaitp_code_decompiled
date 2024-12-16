# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1127_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 635 bytes
from flask import Flask, request
import psycopg2
app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect("dbname=test user=postgres password=secret")


@app.route("/read_file", methods=["GET"])
def read_file():
    filename = request.args.get("filename")
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT pg_read_file('{filename}');")
            file_content = cursor.fetchone()
    return (
     file_content if file_content else "File not found", 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 1127_1.pyc
