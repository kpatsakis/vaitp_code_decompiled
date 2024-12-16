# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1027_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 691 bytes
import logging
from snowflake.connector import connect
logging.basicConfig(level=(logging.DEBUG))
logger = logging.getLogger("snowflake.connector")
user = "your_username"
password = "your_password"
account = "your_account"
passcode = "your_duo_passcode"
conn = connect(user=user,
  password=password,
  account=account,
  passcode=passcode)
cursor = conn.cursor()
try:
    cursor.execute("SELECT CURRENT_VERSION()")
    print(cursor.fetchone())
finally:
    cursor.close()
    conn.close()

# okay decompiling 1027_1.pyc
