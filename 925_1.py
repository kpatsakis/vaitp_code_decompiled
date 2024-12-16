# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 925_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 936 bytes
import psycopg2

def execute_vulnerable_cypher_query(graph_name, cypher_query):
    conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="localhost", port="5432")
    cursor = conn.cursor()
    sql = f"SELECT cypher('{graph_name}', '{cypher_query}')"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return results


graph_name = "my_graph"
cypher_query = "MATCH (n) RETURN n; DROP TABLE users;"
results = execute_vulnerable_cypher_query(graph_name, cypher_query)
print(results)

# okay decompiling 925_1.pyc
