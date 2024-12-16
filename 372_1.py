# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 372_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 606 bytes
import os, sqlite3, tempfile

def create_database():
    db_file = tempfile.mktemp(suffix=".db")
    conn = sqlite3.connect(db_file)
    conn.execute("CREATE TABLE api_keys (key TEXT, bucket_id TEXT)")
    conn.close()
    os.chmod(db_file, 384)
    return db_file


db_path = create_database()

# okay decompiling 372_1.pyc
