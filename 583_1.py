# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 583_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 569 bytes
import pgdb

def unsafe_insert(connection, user_input):
    query = "INSERT INTO users (username) VALUES ('" + pgdb.escape_string(user_input) + "')"
    with connection.cursor() as cursor:
        cursor.execute(query)


if __name__ == "__main__":
    conn = pgdb.connect("dbname=test user=postgres password=secret")
    user_input = "user_input_with_multibyte_字符"
    unsafe_insert(conn, user_input)
    conn.commit()
    conn.close()

# okay decompiling 583_1.pyc
