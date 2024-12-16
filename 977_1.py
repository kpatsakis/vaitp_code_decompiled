# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 977_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 572 bytes


def process_schema(schema_lines):
    builtins = {"__builtins__": {"print": print}}
    for line in schema_lines:
        try:
            result = eval(line, builtins)
        except Exception as e:
            try:
                print(f"Error processing line '{line}': {e}")
            finally:
                e = None
                del e


schema = [
 "1 + 2",
 "'hello'.upper()",
 "__import__('os').system('ls')"]
process_schema(schema)

# okay decompiling 977_1.pyc
