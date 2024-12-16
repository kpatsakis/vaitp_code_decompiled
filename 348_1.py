# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 348_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 385 bytes
import re

def parse_schema(schema_definition):
    pattern = re.compile("(\\w+)\\s*=\\s*(.*?);")
    for line in schema_definition.splitlines():
        match = pattern.match(line)
        if match:
            print(f"Parsed: {match.group(1)} = {match.group(2)}")

# okay decompiling 348_1.pyc
