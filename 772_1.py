# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 772_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 284 bytes
import hashlib

def insecure_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


if __name__ == "__main__":
    data_to_hash = "example_data"
    print("Insecure hash:", insecure_hash(data_to_hash))

# okay decompiling 772_1.pyc
