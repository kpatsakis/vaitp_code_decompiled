# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 117_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 587 bytes


def vulnerable_decode_escape(input_string):
    return input_string.encode("utf-8").decode("unicode_escape")


if __name__ == "__main__":
    input_string = "some_string_with_escape_sequences" + "\x7f" * 2147483648
    try:
        result = vulnerable_decode_escape(input_string)
        print("Decoded string:", result)
    except Exception as e:
        try:
            print("Error:", e)
        finally:
            e = None
            del e

# okay decompiling 117_1.pyc
