# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 351_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 436 bytes


class KeyParser:

    def parse_key(self, key_data):
        expected_length = 10
        try:
            if len(key_data) < expected_length:
                raise ValueError(f"Key field too short: {key_data}")
        except ValueError as e:
            try:
                print(f"Error parsing key: {e}")
            finally:
                e = None
                del e


parser = KeyParser()
parser.parse_key("short_key_data")

# okay decompiling 351_1.pyc
