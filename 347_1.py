# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 347_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 451 bytes
import re
pattern = "SELECT\\s+(?P<columns>[\\w\\s,]+)\\s+FROM\\s+(?P<table>\\w+)(?:\\s+WHERE\\s+(?P<condition>.+))?"

def parse_sql(query):
    match = re.match(pattern, query)
    if match:
        return match.groupdict()


query = "SELECT a, b, c FROM my_table WHERE a = 'value' AND b = 'another_value'"
result = parse_sql(query)
print(result)

# okay decompiling 347_1.pyc
